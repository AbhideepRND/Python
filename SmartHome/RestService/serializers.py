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
        if module_conf == None:
            raise ValueError('Not a valid module')
        pinDetails = module_conf.pin.get(str(validated_data['pin']))
        if pinDetails == None:
            raise ValueError('Pin not found')
        #str(validated_data['key'])+
        data = str(validated_data['pin'])+'&'+ str(validated_data['pinStatus'])+"&MSG"
        mqtt = MqttClientCall()
        print(module_conf.channel.outbound);
        mqtt.callmqttbroker(module_conf.channel.outbound, data)
        return Module(validated_data['moduleName'],validated_data['pin'], validated_data['pinStatus'], validated_data['key'], validated_data['error'])

    def errorObj(self, validated_data):
        print(validated_data['error'])
        return Module(validated_data['moduleName'], validated_data['pin'], validated_data['pinStatus'],
                      validated_data['key'], validated_data['error'])