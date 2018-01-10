from enum import Enum
class Module:
    def __init__(self, name, ip_address, role):
        self.name = name
        self.ip_address = ip_address
        self.role = role
        self.channel = None
        self.status = Status.Inactive
        self.pin = {}

    def setChannel(self,chnl):
        self.channel = chnl

    def setPin(self, pin):
        self.pin[pin.pin_no] = pin


class Channel:
    def __init__(self, inbound, outbound):
        self.inbound = inbound
        self.outbound = outbound


class Pin:
    def __init__(self, pin_no, description=None):
        self.pin_no = pin_no
        self.description = description
        self.status = PinStatus.Low


class Status(Enum):
    Inactive = 'module-inactive'
    Active = 'module-active'

class PinStatus(Enum):
    High = 'High'
    Low = 'Low'