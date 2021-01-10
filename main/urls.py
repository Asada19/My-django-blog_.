from os import name

from django.conf.urls import url
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<str:slug>/', category_detail, name='category'),
    path('post-detail/<int:pk>/', post_detail, name='detail'),
    path('add-post/', add_post, name='add-post'),
    path('update-post/<int:pk>/', update_post, name='update-post'),
    path('delete-post/<int:pk>/', delete_post, name='delete-post'),
    # path('search/', views.post_search, name='search'),
]
