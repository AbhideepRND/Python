from django.conf.urls import url
from django.urls import path

from rest_framework import views

from .views import dashboard, UserList

urlpatterns =[
    url(r'dashboard', dashboard),
    url(r'module', UserList.as_view())

]
