from rest_framework import serializers
from .models import Module


class ModuleSerializer(serializers.Serializer):
    moduleName = serializers.CharField(max_length=10)
    pin = serializers.IntegerField()


def create(self, validated_data):
    print('hello')
    return Module(**validated_data)


def callPy(self):
    print('in py')
