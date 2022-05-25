from django.db.models.signals import post_save
import logging
from .models import Post, Category
from celery import shared_task
import datetime
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from collections import defaultdict

from django.conf import settings

logger = logging.getLogger(__name__)


def send_posts(email_list, posts):
    if isinstance(email_list, str):
        subscriber_list = [email_list, ]
    else:
        subscriber_list = email_list
    email_form = settings.DEFAULT_FROM_EMAIL
    subject = 'В категориях, на которые вы подписаны появились новые статьи'
    text_message = 'В категориях, на которые вы подписаны появились новые статьи'
    render_html_template = render_to_string('send_posts_list.html', {'posts': posts, 'subject': subject})
    msg = EmailMultiAlternatives(subject, text_message, email_form, list(subscriber_list))
    msg.attach_alternative(render_html_template, 'text/html')
    msg.send()


@shared_task
def email_weekly():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    last_week_posts_qs = Post.objects.filter(date__gte=last_week)
    posts_for_user = defaultdict(set)

    for post in last_week_posts_qs:
        for category in post.category.all():
            for user in category.subscribers.all():
                posts_for_user[user].add(post)

    for user, posts in posts_for_user.items():
        send_posts(user.email, posts)


@shared_task
def post_save_post(created, **kwargs):
    post_instance = kwargs['instance']
    subscribers_list = {user.email
                        for category in post_instance.category.all()
                        for user in category.subscribers.all()}
    email_from = settings.DEFAULT_FROM_EMAIL

    if created:
        subject = 'В категориях, на которые вы подписаны появилась новая статья'
        text_message = f'В категориях, на которые вы подписаны появилась новая статья:'
    else:
        subject = 'Произошли изменения в публикации!'
        text_message = f'В публикации произошли изменения! Они доступны  '

    render_html_template = render_to_string('send.html', {'post': post_instance, 'subject': subject, 'text_message': text_message})

    msg = EmailMultiAlternatives(subject, text_message, email_from, list(subscribers_list))
    msg.attach_alternative(render_html_template, 'text/html')
    msg.send()
    post_save(post_save_post, sender=Post)


@shared_task
def notify_managers_posts(instance, action, pk_set, *args, **kwargs):
    if action == 'post_add':
        html_content = render_to_string(
            'mail_create.html',
            {'post': instance,
             }
        )
        for pk in pk_set:
            category = Category.objects.get(pk=pk)
            recipients = [user.email for user in category.subscribers.all()]
            msg = EmailMultiAlternatives(
                subject=f'На сайте NewsPortal новая статья: {instance.postTitle}',

                from_email=settings.DEFAULT_FROM_EMAIL,
                to=recipients
            )
            msg.attach_alternative(html_content, "text/html",)
            msg.send()

    post_save(notify_managers_posts, sender=Post.category.through)
