from .serializers import ModuleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Module
from django.http import JsonResponse


# Create your views here.
class ControlModule(APIView):
    def get(self, request, format=None):
        users = Module("Home", 119,False)
        serializer = ModuleSerializer(users)
        print(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        module = ModuleSerializer(data=data)
        if module.is_valid():
            serialData = ModuleSerializer(module.save())
            print(serialData.data)
            return JsonResponse(serialData.data, status=status.HTTP_200_OK, content_type="application/json")
        return Response(status=status.HTTP_400_BAD_REQUEST)
