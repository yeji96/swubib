from django.db import models
from django.utils import timezone
# Create your models here.

class Comment(models.Model):
    pub_date = models.DateTimeField(default = timezone.now)
    text = models.TextField()