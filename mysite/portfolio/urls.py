from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = (
    #API to post comment
    path('', views.portfolioHome, name='portfolioHome'),
    path('<str:slug>', views.portfolioPost, name='portfolioPost'),
)