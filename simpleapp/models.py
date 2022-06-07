from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.cache import cache

article = 'AR'
news = 'NE'

POSITIONS = [
    (article, 'статья'),
    (news, 'новость'),
]


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_user = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username}'

    def update_rating(self):
        rating_post_author = self.post_set.all().aggregate(Sum('rating_post'))['rating_post__sum']
        rating_comment = self.comment_set.all().aggregate(Sum('rating_comment'))['rating_comment__sum']
        rating_comment_post = Comment.objects.filter(post__author__pk=self.pk).aggregate(Sum('rating_comment'))[
            'rating_comment__sum']
        self.rating_user = rating_post_author * 3 + rating_comment + rating_comment_post
        self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, related_name='subscribers')

    def __str__(self):
        return f'{self.category_name}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    select = models.CharField(max_length=2, choices=POSITIONS, default=news)
    date = models.DateTimeField('дата создания', auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    header_post = models.CharField('название', max_length=255)
    text_post = models.TextField('текст')
    rating_post = models.IntegerField('рейтинг', default=0)

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return self.text_post[:124] + '...'

    def __str__(self):
        return f'{self.header_post.title()}: {self.text_post[:20]}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField('текст')
    date_comment = models.DateTimeField('дата', auto_now_add=True)
    rating_comment = models.IntegerField('рейтинг', default=0)

    def __str__(self):
        return f'{self.user.username}: {self.text_comment[:20]}'

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()
