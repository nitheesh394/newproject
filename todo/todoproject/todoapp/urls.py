"""todoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('', views.add, name='home'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),

    #class paths

    path('homepage/', views.listview.as_view(), name= 'homepage'),
    path('details/<int:pk>/', views.detailview.as_view(), name= 'detailpage'),
    path('update/<int:pk>/', views.updateview.as_view(), name= 'updatepage'),
    path('delete/<int:pk>/', views.deleteview.as_view(), name= 'deletepage'),

]
