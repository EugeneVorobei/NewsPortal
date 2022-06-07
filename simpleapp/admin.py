from django.contrib import admin
from .models import Category, Post, Author, Comment, PostCategory


class PostAdmin(admin.ModelAdmin):
    list_display = ('header_post', 'author', 'date', 'select', 'rating_post')
    list_filter = ('author', 'date', 'select')
    search_fields = ('header_post', 'author', 'category__category_name')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating_user')
    list_filter = ('user',)
    search_fields = ('user',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'date_comment', 'text_comment')
    list_filter = ('post', 'user', 'date_comment', 'rating_comment')
    search_fields = ('post', 'user')


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('post', 'category')
    list_filter = ('post', 'category')
    search_fields = ('post', 'category')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
