import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("localhost",1883,60)
client.publish("192.168.1.1/data", "sfbshfjsbvdfhvsjfhsvdjfvjsdvfsjdfvjvsjfvsdvfvsjvfj!");
client.disconnect();