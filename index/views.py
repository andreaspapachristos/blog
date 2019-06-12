# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import  User

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')
    }

    return render(request, 'index/article.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'index/article.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']






