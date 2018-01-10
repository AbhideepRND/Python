from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Hello, World")

def login(request):
    return HttpResponse("Login Page")
