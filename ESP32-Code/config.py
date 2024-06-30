""""Configuration file for pin assignments and other constants"""
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Wi-Fi settings
WIFI_SSID = os.getenv('WIFI_SSID')
WIFI_PASSWORD = os.getenv('WIFI_PASSWORD')

# Sensors pin assignments
SOIL_MOISTURE_1_PIN = 32
SOIL_MOISTURE_2_PIN = 33
SOIL_MOISTURE_3_PIN = 34
SOIL_MOISTURE_4_PIN = 35

# Valve pin
VALVE_PIN = 25

# MQTT settings
MQTT_BROKER = os.getenv('MQTT_BROKER')
MQTT_PORT = os.getenv('MQTT_PORT')
MQTT_CLIENT_ID_ESP32 = os.getenv('MQTT_CLIENT_ID_ESP32')
MQTT_CLIENT_ID_FLASK = os.getenv('MQTT_CLIENT_ID_FLASK')
MQTT_TOPIC_SENSOR = os.getenv('MQTT_TOPIC_SENSOR')
MQTT_TOPIC_CONTROL = os.getenv('MQTT_TOPIC_CONTROL')
