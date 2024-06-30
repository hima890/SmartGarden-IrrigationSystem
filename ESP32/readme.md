# Smart Garden Irrigation System - ESP32 Code

This folder contains the ESP32 code for the Smart Garden Irrigation System project. The ESP32 is used to monitor soil moisture levels and control a water pump via MQTT communication.

## Folder Structure

```
ESP32/
│
├── config.py
├── mqtt_client.py
├── sensors.py
├── pump.py
├── utility/
│   ├── on_message_function.py
│   ├── send_sensor_data_function.py
│   └── check_messages_function.py
└── wifi_setup.py
```

## Files and Directories

### 1. `config.py`

This file contains configuration settings for the MQTT client, including the broker address, port, client ID, and MQTT topics.

### 2. `mqtt_client.py`

This is the main file that initializes the MQTT client, sets up the sensor and pump, handles MQTT communication, and runs the main loop for the project.

### 3. `sensors.py`

This file contains the `SoilMoistureSensor` class, which reads soil moisture levels from the sensors.

### 4. `pump.py`

This file contains the `Pump` class, which controls the water pump based on MQTT messages.

### 5. `utility/`

This directory contains utility functions used by `mqtt_client.py`:

- `on_message_function.py`: Contains the `on_message` function to handle incoming MQTT messages.
- `send_sensor_data_function.py`: Contains the `send_sensor_data` function to publish sensor data to the MQTT broker.
- `check_messages_function.py`: Contains the `check_messages` function to check for incoming MQTT messages.

### 6. `wifi_setup.py`

This file contains code to connect the ESP32 to a WiFi network.

## Setup Instructions

### Prerequisites

- ESP32 board
- MicroPython firmware installed on the ESP32
- Soil moisture sensors
- Water pump
- MQTT broker (e.g., HiveMQ, Mosquitto)

### Step-by-Step Guide

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```sh
   git clone https://github.com/yourusername/SmartGarden-IrrigationSystem.git
   cd SmartGarden-IrrigationSystem/ESP32
   ```

2. **Install Dependencies**

   Install necessary MicroPython libraries on your ESP32:

   ```sh
   pip install micropython-umqtt.simple
   ```

3. **Configure WiFi Settings**

   Edit `wifi_setup.py` to include your WiFi credentials:

   ```python
   import network
   import time

   ssid = 'your_wifi_ssid'
   password = 'your_wifi_password'

   sta_if = network.WLAN(network.STA_IF)
   sta_if.active(True)
   sta_if.connect(ssid, password)

   while not sta_if.isconnected():
       print('Connecting to WiFi...')
       time.sleep(1)

   print('WiFi connected:', sta_if.ifconfig())
   ```

4. **Configure MQTT Settings**

   Edit `config.py` to include your MQTT broker settings:

   ```python
   MQTT_BROKER = 'your_mqtt_broker'
   MQTT_PORT = 1883
   MQTT_CLIENT_ID_ESP32 = 'your_client_id_esp32'
   MQTT_TOPIC_SENSOR = 'sensor/moisture'
   MQTT_TOPIC_CONTROL = 'valve_control'
   ```

5. **Upload Code to ESP32**

   Use an appropriate tool (e.g., `ampy`, `rshell`, `mpremote`) to upload the files to your ESP32:

   ```sh
   ampy --port /dev/ttyUSB0 put config.py
   ampy --port /dev/ttyUSB0 put mqtt_client.py
   ampy --port /dev/ttyUSB0 put sensors.py
   ampy --port /dev/ttyUSB0 put pump.py
   ampy --port /dev/ttyUSB0 put wifi_setup.py
   ampy --port /dev/ttyUSB0 put utility/
   ```

6. **Run the Code**

   Access the ESP32 REPL (Read-Eval-Print Loop) and run the main file:

   ```sh
   import mqtt_client
   mqtt_client.main_loop()
   ```

## Usage

Once the code is running, the ESP32 will:

- Connect to the specified WiFi network.
- Connect to the MQTT broker.
- Periodically read soil moisture sensor data.
- Publish the sensor data to the MQTT topic.
- Listen for control messages on the MQTT topic to open or close the water pump.

## Troubleshooting

- **WiFi Connection Issues**: Ensure the WiFi credentials are correct and the ESP32 is within range of the WiFi network.
- **MQTT Connection Issues**: Ensure the MQTT broker settings are correct and the broker is running.
- **Sensor Data Issues**: Verify the sensors are connected properly and the correct pins are used in the code.

## License

This project is licensed under the GPT License. See the LICENSE file for more details.
