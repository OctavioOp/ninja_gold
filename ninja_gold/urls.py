from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.login),
    path('/home',views.home),
    path('/reset',views.login),
    path('/process_money/<uri>',views.process,name='money'),
    path('/bet', views.bet)

]