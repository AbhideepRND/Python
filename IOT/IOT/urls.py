"""IOT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include

from .view.RequestController import welcome
from .view.RequestController import login
from django.template.backends.django import DjangoTemplates

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^welcome', welcome), # here r denote the regular expression in url.^is the starting point and $- is the end point
    url(r'^$', login),
    url(r'^esp8266/', include('esp8266.urls'))
]
