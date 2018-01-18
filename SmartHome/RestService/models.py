from django.db import models
# Create your models here.

class Module(object):

    def __init__(self, moduleName, pin, pinStatus, key, error):
        self.moduleName = moduleName
        self.pin = pin
        self.pinStatus=pinStatus
        self.key=key
        self.error=error
