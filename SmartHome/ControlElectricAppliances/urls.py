from django.conf.urls import url
from django.urls import path

from .views import dashboard, moduledetails

urlpatterns =[
    url(r'dashboard', dashboard),
    url(r'componentdetails', moduledetails)
]
