from django.db import models
from django.db.models import aggregates
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User

class BrailleInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    filename = models.CharField(max_length=255,default=None)
    braille_draft = models.TextField()
    braille_text = models.TextField()
    date_saved = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'BrailleInfo'


class ActivityHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_log = models.CharField(max_length=255)
    date_log = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'ActivityHistory'
    