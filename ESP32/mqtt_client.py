""" MQTT client for sending sensor data,
calculating averages, and responding to commands.
"""
import time
import ujson
from umqtt.simple import MQTTClient
from sensors import SoilMoistureSensor
from pump import Pump
from utility.on_message_function import on_message
from utility.send_sensor_data_function import send_sensor_data
from utility.check_messages_function import check_messages
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

# MQTT Setup
client = MQTTClient(
    MQTT_CLIENT_ID_ESP32,
    MQTT_BROKER,
    port=MQTT_PORT
    )


# MQTT Callback Setup
# Wrapper Function (on_message_callback)
def on_message_callback(topic, msg):
    """
        A new function on_message_callback that takes topic
        and msg as parameters (as expected by the MQTT client)
        and calls on_message with the valve object.

        Args:
            topic (bytes): The topic that the message was published to.
            msg (bytes): The actual message payload.

        Returns:
            No return.
    """
    on_message(topic, msg, pump)


# Set the callback to the wrapper Function
client.set_callback(on_message_callback)


# Try to connect to the MQTT server
try:
    client.connect()
    client.subscribe(MQTT_TOPIC_CONTROL.encode())
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")


# Main loop function
def main_loop():
    while True:
        send_sensor_data(sensors_data_reading, sensors_data_avreg, pump_status)
        check_messages(client)
        # Adjust the interval as needed
        time.sleep(60)


if __name__ == '__main__':
    main_loop()
