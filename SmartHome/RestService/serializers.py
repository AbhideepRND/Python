from rest_framework import serializers
from .models import Module
from ControlElectricAppliances.util.mqttclient import MqttClientCall
from SmartHome import config


class ModuleSerializer(serializers.Serializer):
    moduleName = serializers.CharField(max_length=10)
    pin = serializers.IntegerField()
    key=serializers.IntegerField()
    pinStatus = serializers.BooleanField()
    error=serializers.CharField(allow_null=True)

    def create(self, validated_data):
        module_conf = config.espModuleConfig.get(validated_data['key'])
        data = '{ "pin":"'+str(validated_data['pin'])+'","status":"'+ str(validated_data['pinStatus'])+'"}'
        mqtt = MqttClientCall()
        mqtt.callmqttbroker(module_conf.channel.inbound, data)
        return Module(validated_data['moduleName'],validated_data['pin'], validated_data['pinStatus'], validated_data['key'], validated_data['error'])
