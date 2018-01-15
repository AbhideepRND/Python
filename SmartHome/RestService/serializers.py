from rest_framework import serializers
from .models import Module


class ModuleSerializer(serializers.Serializer):
    moduleName = serializers.CharField(max_length=10)
    pin = serializers.IntegerField()

    def create(self, validated_data):
        print(validated_data['moduleName'])
        print(validated_data['pin'])
        return Module(validated_data['moduleName'],validated_data['pin'])
