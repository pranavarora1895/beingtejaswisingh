from django.contrib import admin
from .models import Comment
# Register your models here.

class CommentDisplay(admin.ModelAdmin):

    list_display = ('id', 'post_title', 'name', 'email', 'comment', 'reply', 'is_postable',)
    search_fields = ('post_title', 'name',)
    list_filter = ('post_title', 'is_postable',)
    list_display_links = ('id', 'post_title', 'name', 'email',)
    list_editable = ('is_postable',)


admin.site.register(Comment, CommentDisplay)
