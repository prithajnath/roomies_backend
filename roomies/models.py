from __future__ import unicode_literals
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.files import File
from django.db import models
from roomies_backend.settings import BASE_DIR
import os
# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        

class UserManager(models.Manager):
    def create_userprofile(self,user):
        profile = self.create(user=user)
        profile.avatar.save(os.path.join(BASE_DIR,'defaultpic.png'),File(open(os.path.join(BASE_DIR,'defaultpic.png'),'r')))
        return profile
        
class UserProfile(models.Model):
    user   = models.OneToOneField(User)
    avatar = models.ImageField()
    
    objects = UserManager()
    
class UserMatches(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match_username = models.CharField(max_length=100)
    
    def __repr__(self):
        return self.match_username
    
    def __str__(self):
        return self.match_username
        
    def get_match_userid(self):
        return User.objects.get(username=self.match_username).pk