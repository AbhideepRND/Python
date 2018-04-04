from .serializers import ModuleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Module
from django.http import JsonResponse
from SmartHome import config
import json
from django.core import serializers


# Create your views here.
class ControlModule(APIView):
    def get(self, request, format=None):
        try:
            key = int(request.query_params.get('key', None))
            module_details = config.espModuleConfig[key]
            pin_list=[]
            for k,v in module_details.pin.items():
                pin_list.append(Module(module_details.name, k, v.status, key, None))
            serializer = ModuleSerializer(pin_list, many=True)
            print(serializer.data)
        except Exception as e:
            serializer = ModuleSerializer(Module(None, None, None,key, str(e)))
            return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        module = ModuleSerializer(data=data)
        try:
            if module.is_valid():
                serialData = ModuleSerializer(module.save())
                print(serialData.data)
                return JsonResponse(serialData.data, status=status.HTTP_200_OK, content_type="application/json")
        except Exception as e:
                print(e.args)
                data['error']=str(e.args[0])
                serializer = ModuleSerializer(module.errorObj(data))
                return JsonResponse(serializer.data, safe=False, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")




#{"error":null,
#"key":10,
#"moduleName":"Bed Room",
#"pinStatus":true,
#"pin":18}