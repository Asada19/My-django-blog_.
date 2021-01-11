from os import name

from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import RegisterView, SignInView, profile
from . import views
from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('add-post/', add_post, name='add-post'),
    path('update-post/<int:pk>/', update_post, name='update-post'),
    path('delete-post/<int:pk>/', DeletePostView.as_view(), name='delete-post'),
    path('sign-up/', RegisterView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('myprofile/', profile, name='profile'),
]
