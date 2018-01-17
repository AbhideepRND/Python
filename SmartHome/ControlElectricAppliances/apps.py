from django.apps import AppConfig
from ControlElectricAppliances.xmlreader.filereader import ReadSaxElement
from SmartHome import config
from .util.mqttconfig import Subscriber

class ControlelectricappliancesConfig(AppConfig):
    name = 'ControlElectricAppliances'

    def ready(self):
        print('In Web config')

        config.espModuleConfig = ReadSaxElement.loadXmlConfig(object, "module_config.xml")
        for (k, v) in config.espModuleConfig.items():
            module = Subscriber(v.ip_address, v.channel.inbound)
            module.start()
            print(v.channel.inbound)
            for (i, j) in v.pin.items():
                print(j.pin_no + " --- " + j.description)
