from django.forms import ModelForm, BooleanField
from .models import Post


class PostForm(ModelForm):
    check_box = BooleanField(label='Ало, Галочка!')

    class Meta:
        model = Post
        fields = ['header_post', 'select', 'author', 'category', 'text_post', 'check_box']
