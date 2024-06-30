"""Function to send sensor data"""

def send_sensor_data(sensors_data_reading, sensors_data_avreg, pump_status):
    """
    Send sensor data to the MQTT topic in JSON format.

    Args:
        sensors_data_reading (list): A list of current moisture sensor readings.
        sensors_data_avreg (float): The average value of the moisture sensor readings.
        pump_status (str or bool): The current status of the pump, typically represented as a string or boolean.

    Returns:
        None

    Example:
        sensors_data_reading = [450, 460, 470]
        sensors_data_avreg = sum(sensors_data_reading) / len(sensors_data_reading)
        pump_status = 'ON'
        
        send_sensor_data(sensors_data_reading, sensors_data_avreg, pump_status)

    Raises:
        Exception: If there is an error in publishing the data.
    """

    # Set the data as JSON format
    data = {
        'moisture_values': sensors_data_reading,
        'average_moisture': sensors_data_avreg,
        'pump_status': pump_status
    }

    try:
        client.publish(config.MQTT_TOPIC_SENSOR.encode(),
                       ujson.dumps(data))
        print('Data sent:', data)
    except Exception as e:
        print(f"Failed to publish data: {e}")
