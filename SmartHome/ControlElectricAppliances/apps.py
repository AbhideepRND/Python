from django.apps import AppConfig
from ControlElectricAppliances.xmlreader.filereader import ReadSaxElement
from SmartHome import config
from .util.mqttconfig import Subscriber
from ControlElectricAppliances.util.SmartHomeSchedular import PeriodicScheduler

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
        INTERVAL = 45 # every second
        periodic_scheduler = PeriodicScheduler()
        periodic_scheduler.setup(INTERVAL, periodic_scheduler.periodic_event) # it executes the event just once
        periodic_scheduler.start() # it starts the scheduler