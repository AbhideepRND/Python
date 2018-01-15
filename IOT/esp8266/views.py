from django.shortcuts import render

from .models import Module
from django.http import Http404

from .serializers import ModuleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer




# Create your views here.

def dashboard(request):
    return render(request, "esp8266/home.html",
                  {'message': "Hi How are you?"})


class UserList(APIView):

    def get(self, request, format=None):
        users = Module("Home",119)
        serializer = ModuleSerializer(users)
        print(serializer.data)
        #json = JSONRenderer.render(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        print(data)
        module = ModuleSerializer(data=data)
        if module.is_valid():
            #print(module.data.moduleName)
            module.save()
            module.callPy()
            return Response(module.data, status=status.HTTP_201_CREATED)
       # serializer = ModuleSerializer(data=request.DATA)
        #print(serializer.data.moduleName)
        #if serializer.is_valid():s
        #   return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
