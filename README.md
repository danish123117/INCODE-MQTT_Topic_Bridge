# MQTT Client for Topic Modification

This Python script subscribes to MQTT topics and modifies the received messages before republishing it to new topics. The purpose is to remap the topics so that it can help in integrating Polar data logger topics to FIWARE IOT agent compliant topic structure

## Features

- Subscribes to multiple MQTT topics.
- Modifies and republishes received message topic by appending "/attrs" to the topic.

## Prerequisites

- Python 3.x
- Paho MQTT library (`paho-mqtt`)


## Environment Variables

- `POLAR_H10_API_KEY`: (Optional) The MQTT topic prefix. Default is "danishabbas2".
- `MQTT_BROKER_NAME`: (Optional) The hostname or IP address of the MQTT broker. Default is "mosquitto".
- `MQTT_BROKER_PORT`: (Optional) The port number of the MQTT broker. Default is 1883.


