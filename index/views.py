# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post
from  django.http.response import HttpResponse
from django.views.generic import ListView, CreateView
from users.views import UserRegisterForm
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def home(request):
#     context = {
#         'posts': Post.objects.all().order_by('-date_posted')
#     }
#
#     return render(request, 'index/article.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'index/article.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def post(self, request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')

                return HttpResponse()
        else:
            form = UserRegisterForm()
        return render(request, 'users/modal.html', {'form': form})




