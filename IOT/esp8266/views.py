from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, "esp8266/home.html",
                  {'message': "Hi How are you?"})