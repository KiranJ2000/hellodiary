from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.db.models.signals import pre_save

from hellodiary.utils import unique_slug_generator

# Create your models here.

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length = 80, null=True)
    date_created = models.CharField(max_length=100,null=True)
    diary_entry = models.TextField(null=True)

    def __str__(self):
        return self.title
    

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Diary)


