import paho.mqtt.client as mqtt


# This is the Publisher

class MqttClientCall:
    def callmqttbroker(self, queue_name, message):
        client = mqtt.Client()
        client.connect("localhost", 1883)
        client.publish(queue_name, message);
        client.disconnect();
