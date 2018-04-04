import sched
import datetime, time
import os
from SmartHome import config
from ControlElectricAppliances.xmlreader.xmlstructure import Status
from threading import Thread


class PeriodicScheduler(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def setup(self, interval, action, actionargs=()):
        action(*actionargs)
        self.scheduler.enter(interval, 1, self.setup,
                             (interval, action, actionargs))

    def run(self):
        self.scheduler.run()

    def periodic_event(self):
        for (k, v) in config.espModuleConfig.items():
            response = os.system("ping -c 1 " + v.ip_address);
            if response == 0:
                print("is up!")
                #hostname, 'is up!'
                v.status = Status.Active
            else:
                print("is down!")
                # hostname, 'is down!'
                v.status = Status.Inactive


#INTERVAL = 15 # every second
#periodic_scheduler = PeriodicScheduler()
#periodic_scheduler.setup(INTERVAL, periodic_scheduler.periodic_event) # it executes the event just once
#periodic_scheduler.run() # it starts the scheduler