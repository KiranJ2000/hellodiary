from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 80, null=True)
    date_created = models.CharField(max_length=100,null=True)
    diary_entry = models.TextField(null=True)

