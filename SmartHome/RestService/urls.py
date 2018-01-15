from django.conf.urls import url

from rest_framework import views

from .views import ControlModule

urlpatterns =[
    url(r'controlModule', ControlModule.as_view())
]