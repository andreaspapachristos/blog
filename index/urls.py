from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('modal/', views.modal, name='modal'),

]

