from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class MyInfo(models.Model):

    website_title = models.CharField(max_length=50, blank=True)
    address = models.TextField()
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    other_info = models.TextField(blank=True)
    about_summary = models.TextField(blank=True)
    fb_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)
    insta_link = models.URLField(max_length=255)
    linkedin_link = models.URLField(max_length=255)
    youtube_link = models.URLField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.website_title

class About(models.Model):

    about_photo = models.ImageField(upload_to='media/about/%Y/%m')
    about_me = RichTextField()
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return ("About me "+ str(self.created_date))