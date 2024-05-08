import os
import paho.mqtt.client as mqtt
def on_message(client, userdata, message):
    received_topic = message.topic
    received_payload = message.payload.decode("utf-8")
    modified_topic = received_topic + "/attrs"
    client.publish(modified_topic, received_payload)

def main():
    danishabbas_topic = os.getenv("POLAR_H10_API_KEY", "danishabbas2")
    broker = os.getenv("MQTT_BROKER_NAME", 'localhost')
    port = int(os.getenv("MQTT_BROKER_PORT", 1880))
    broker_address = broker
    broker_port = port
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    client.on_message = on_message
    client.connect(broker_address, broker_port)
    client.subscribe(f"json/{danishabbas_topic}/ecg")
    client.subscribe(f"json/{danishabbas_topic}/hr")
    client.subscribe(f"json/{danishabbas_topic}/acc")
    client.loop_forever()

if __name__ == "__main__": 
    main()