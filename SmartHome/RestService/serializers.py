from rest_framework import serializers
from .models import Module


class ModuleSerializer(serializers.Serializer):
    moduleName = serializers.CharField(max_length=10)
    pin = serializers.IntegerField()
    pinStatus = serializers.BooleanField()

    def create(self, validated_data):
        print(validated_data['moduleName'])
        print(validated_data['pin'])
        print(validated_data['pinStatus'])
        return Module(validated_data['moduleName'],validated_data['pin'], validated_data['pinStatus'])
