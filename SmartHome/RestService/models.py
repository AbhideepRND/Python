from django.db import models

# Create your models here.

class Module(object):

    def __init__(self, moduleName, pin):
        self.moduleName = moduleName
        self.pin = pin