from django.contrib import admin
from .models import Post
from django.utils.html import format_html
# Register your models here.

class PostAdmin(admin.ModelAdmin):

    def homepage_photo(self, object):
        return format_html('<img src="{}" width=50 />'.format(object.photo_home.url))

    list_display = ('id', 'title', 'category', 'is_featured', 'created_date', 'homepage_photo',)
    search_fields = ('title', 'category',)
    list_filter = ('category', 'is_featured',)
    list_display_links = ('id', 'title', 'homepage_photo',)
    list_editable = ('is_featured',)

admin.site.register(Post, PostAdmin)