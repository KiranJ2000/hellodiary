from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.db.models.signals import pre_save

# Create your models here.

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length = 80, null=True)
    date_created = models.DateField(auto_now_add=True, editable=False, null=True)
    diary_entry = models.TextField(null=True)

    def __str__(self):
        return self.title
    


