from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.login),
    path('/home',views.home),
    path('/farm',views.farm),
    path('/cave',views.cave),
    path('/house',views.house),
    path('/casino',views.casino),
    
]