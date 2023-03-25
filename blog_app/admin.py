from django.contrib import admin
from .models import Author, Post, Comment

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author')
    list_filter = ('pub_date', 'author')
    search_fields = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'pub_date', 'text')
    list_filter = ('pub_date', 'author', 'post')
    search_fields = ('text',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
