from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.
class Post(models.Model):


    title = models.CharField(max_length=255)
    summary = RichTextField()
    category = models.CharField(max_length=255, blank=True)
    photo_home = models.ImageField(upload_to='media/home/%Y/%m')
    photo_blogpage = models.ImageField(upload_to='media/blogpage/%Y/%m')
    content = RichTextField()
    author = models.CharField(max_length=255, blank=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    
