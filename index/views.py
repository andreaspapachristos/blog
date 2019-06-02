# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')
    }

    return render(request, 'index/article.html', context)
