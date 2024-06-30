# Configuration file for pin assignments and other constants

# Wi-Fi settings
WIFI_SSID = 'Wokwi-GUEST'
WIFI_PASSWORD = ''

# Sensors pin assignments
SOIL_MOISTURE_1_PIN = 32
SOIL_MOISTURE_2_PIN = 33
SOIL_MOISTURE_3_PIN = 34
SOIL_MOISTURE_4_PIN = 35

# Valve pin
VALVE_PIN = 25

# MQTT settings
MQTT_BROKER = 'bcfe325a54b74177a07b98e7235cb5ea.s1.eu.hivemq.cloud'
MQTT_PORT = 8883
MQTT_CLIENT_ID_ESP32 = 'ESP32_Client'
MQTT_CLIENT_ID_FLASK = 'Flask_Server'
MQTT_TOPIC_SENSOR = 'sensor/moisture'
MQTT_TOPIC_CONTROL = 'valve/control'
