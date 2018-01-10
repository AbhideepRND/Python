from django.conf.urls import url
from django.urls import path

from .views import dashboard

urlpatterns =[
    url(r'dashboard', dashboard)

]
