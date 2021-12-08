from django.db import models
from webpages.models import Post
from datetime import datetime
# Create your models here.

class Comment(models.Model):

    post_title = models.ForeignKey(Post, related_name="post", null=True ,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    comment = models.TextField()
    is_postable = models.BooleanField(default=False)
    reply = models.TextField(blank=True)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.name


