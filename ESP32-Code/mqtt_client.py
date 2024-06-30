""" MQTT client for sending sensor data, calculating averages,
and responding to commands
"""
import time
import ujson
from umqtt.simple import MQTTClient
from sensors import SoilMoistureSensor
from pump import Pump
from config import (MQTT_CLIENT_ID_ESP32,
                    MQTT_BROKER,
                    MQTT_PORT,
                    MQTT_TOPIC_CONTROL)

# Initialize sensor classe
soil_moisture_sensor = SoilMoistureSensor()
sensors_data_reading = soil_moisture_sensor.read_moisture()
sensors_data_avreg = soil_moisture_sensor.avg_sensor_data()

# Initialize pump class
pump = Pump()
pump_status = pump.status

# MQTT Callback
def on_message(topic, msg):
    """
    Control the pump status based on the MQTT message.

    Args:
        topic(object): Un umqtt object message was published to.
        msg(object):  Un umqtt object that contains:
            msg.topic(object): The topic that the message was published to.
            msg.payload(object): The actual message payload.

    Returns:
        No return.
    """
    # Echo the topic and the msg data
    print((topic, msg))
    # Check the message and change the pump status
    if msg == b'open_valve':
        pump.open()
    elif msg == b'close_valve':
        pump.close()

# MQTT Setup
client = MQTTClient(
    MQTT_CLIENT_ID_ESP32,
    MQTT_BROKER,
    port=MQTT_PORT
    )
client.set_callback(on_message)

# Try to connect to the MQTT server
try:
    client.connect()
    client.subscribe(MQTT_TOPIC_CONTROL.encode())
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")

