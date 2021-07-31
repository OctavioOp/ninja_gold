from random_word.views import home, login
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login),
    path('/login',views.login),
    path('/home',views.home),
]