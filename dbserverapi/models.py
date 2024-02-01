from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    subreddit = models.CharField(max_length=255)
    url = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    selftext = models.TextField()
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   