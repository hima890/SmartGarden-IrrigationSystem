"""
This module interface with soil moisture sensors.
"""

from machine import ADC
from config import (SOIL_MOISTURE_1_PIN,
                    SOIL_MOISTURE_2_PIN,
                    SOIL_MOISTURE_3_PIN,
                    SOIL_MOISTURE_4_PIN
                    )


class SoilMoistureSensor:
    """
    This class serves as un interface with soil moisture sensors.
    It provides attributes and methods to intract with the senors.
    """
    def __init__(self, pin):
        """
        Initializes a new instance of the SoilMoistureSensor class.
        Attributes:
            adc : Un ADC object from machine lib.
        """
        # Set the Adc pins
        self.adc_sensor1 = ADC(SOIL_MOISTURE_1_PIN)
        self.adc_sensor2 = ADC(SOIL_MOISTURE_2_PIN)
        self.adc_sensor3 = ADC(SOIL_MOISTURE_3_PIN)
        self.adc_sensor4 = ADC(SOIL_MOISTURE_4_PIN)

        # Configure ADC to measure 0-3.3V
        self.adc_sensor1.atten(ADC.ATTN_11DB)
        self.adc_sensor2.atten(ADC.ATTN_11DB)
        self.adc_sensor3.atten(ADC.ATTN_11DB)
        self.adc_sensor4.atten(ADC.ATTN_11DB)

    def read_moisture(self):
        """
        Read the data from the SoilMoistureSensor.

        Args:
            No args.

        Returns:
            data(list): A list of all the sensors reading value.
        """
        sensor_1_data = self.adc_sensor1.read()
        sensor_2_data = self.adc_sensor2.read()
        sensor_3_data = self.adc_sensor3.read()
        sensor_4_data = self.adc_sensor4.read()

        data = [sensor_1_data,
                sensor_2_data,
                sensor_3_data,
                sensor_4_data
                ]

        return (data)

    def avg_sensor_data(self, data):
        """
        Calculate the sensors data avreg value .

        Args:
            data (list): List representing the sensor object.

        Returns:
            data_avg: The data averg value.
        """
        data_sum = 0
        for value in data:
            data_sum += value

        #  Use len(data) to make it adaptable to different data lengths
        data_avg = data_sum / len(data)
        return (data_avg)
