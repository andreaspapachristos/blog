# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post, User
from django.http.response import JsonResponse
from django.views.generic import ListView, CreateView
from django.shortcuts import redirect
from django.core.validators import validate_email
from django.http import HttpResponse
from . import file


# Create your views here.

# αλλαγή σε class based views απο function based views

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


def modal(request):
    # η μέθοδος είναι η POST αλλά καθορίζεται από το js κώδικα (ajax) οπότε και είναι περιττο το if
    #  if request.method == 'POST':

    try:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        data1 = {
            "exists": User.objects.filter(username__iexact=username).exists(),
        }
        # πραγματοποιεί έλεγχο αν υπάρχει ήδη χρήστης με το ίδιο username. Ο έλεγχος γίνεται ασύγχρονα οπότε και το
        # αποτέλεσμα επιστρέφει κατόπιν του submit
        if data1['exists']:
            data1['error_message'] = 'A user with this username already exists.'
            return JsonResponse(data1)

        else:
            file.write_user(username, email, password)
            return redirect('/')
    # η κανονική λειτουργία της σελιδας θα δημιουργεί τον χρήστη στην βάση με τον παρακάτω κώδικα, προς στιγμήν απλά
    # κρατάω τις εγγραφες σε ένα αρχείο για δοκιμή. user = User.objects.create( username=username, email=email,
    # password=password ) user.save()

    # σε περίπτωση keyerror καταχωρεί default τιμές
    except KeyError:
        username = 'andreas'
        email = 'admin@linuxdude.gr'
        password = '12345678'
        file.write_user(username, email, password)
        return redirect('/')
