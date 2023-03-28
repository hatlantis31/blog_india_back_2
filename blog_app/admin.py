from django.contrib import admin
from .models import Author, Post, Comment, Photo

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'pub_date', 'text')
    list_filter = ('pub_date', 'author', 'post')
    search_fields = ('text',)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('post', 'image', 'caption')
    list_filter = ('post',)
    search_fields = ('caption',)

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author')
    list_filter = ('pub_date', 'author')
    search_fields = ('title',)
    inlines = [PhotoInline]  # Add this line

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Photo, PhotoAdmin)
