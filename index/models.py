# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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


