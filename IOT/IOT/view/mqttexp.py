import paho.mqtt.client as mqtt
from threading import Thread


class Subscriber(Thread):
    ipaddress = ''
    url = ''

    def __init__(self, ipaddress, url):
        Thread.__init__(self)
        self.ipaddress = ipaddress
        self.url = url

    def run(self):
        client = mqtt.Client()
        client.connect("localhost", 1883, 60)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe(self.url)

    def on_message(self, client, userdata, msg):
        print(msg.payload)


subscriber1= Subscriber("192.168.1.1","192.168.1.1/data")
subscriber2= Subscriber("192.168.1.3","192.168.1.3/data")
subscriber1.start()
subscriber2.start()
print("hello")

