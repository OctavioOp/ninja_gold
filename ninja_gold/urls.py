from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.login),
    path('/home',views.home),
    path('/process_money/<uri>',views.process),

]