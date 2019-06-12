# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import logging


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_read = models.IntegerField(default=3)
    category = models.CharField(max_length=40)
    email = models.EmailField(User.get_email_field_name(), default='admin@linuxdude.gr')

    def __str__(self):
        return self.title

    def readFile(self):
        user = User.objects.filter(username='master').first()
        post = Post.objects.create(author=user)
        f = open('/home/master/Downloads/test', 'r')
        post.title = f.readline()
        post.category = f.readline()
        post.content = f.readline()
        f.close()
        return self.save()


def save_post(sender, instance, **kwargs):
    logging.getLogger(__name__).error('error')


post_save.connect(save_post, sender=Post)
