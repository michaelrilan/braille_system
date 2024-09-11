from django.db import models
from django.db.models import aggregates
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_faculty = models.BooleanField(verbose_name='is_faculty', default=False)
    is_student = models.BooleanField(verbose_name='is_student', default=False)
    deleteflag = models.BooleanField(default=False)
    class Meta:
        db_table = 'UserProfile'

class BrailleInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    filename = models.CharField(max_length=255,default=None)
    braille_draft = models.TextField()
    braille_text = models.TextField()
    date_saved = models.DateField(auto_now_add=True)
    deleteflag = models.BooleanField(default=False)
    class Meta:
        db_table = 'BrailleInfo'


class ActivityHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_log = models.CharField(max_length=255)
    date_log = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'ActivityHistory'


class SharedBraille(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='braille_owner')
    shared_to_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='brailler_receiver')
    braille_info = models.ForeignKey(BrailleInfo,on_delete=models.CASCADE)
    class Meta:
        db_table = 'SharedBraille'
    