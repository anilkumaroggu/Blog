from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length =100)
    title = models.CharField(max_length =200)
    text = models.TextField()
    tag=models.TextField(default=None)
    
    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
