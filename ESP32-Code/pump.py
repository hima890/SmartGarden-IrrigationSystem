"""
This module control water pump.
"""
from machine import Pin
from config import VALVE_PIN


class Pump:
    """
    This class serves as un interface with water pump.
    It provides attributes and methods to intract with the water pump relay.
    """
    def __init__(self):
        """
        Initializes a new instance of the Pump class.
        Attributes:
            valve(object) : A machine object to control the MCU pins.
            status(string): A string value track the pump current status.
        """
        # Set the pin mode (output)
        self.valve = Pin(VALVE_PIN, Pin.OUT)
        # Init the pin with off state(0)
        self.valve.off()
        # Set the pump status
        self.status = "off"

    def open(self):
        """
        Turn on the water pump relay on.

        Args:
            No args.

        Returns:
            No return.
        """
        self.valve.on()
        self.status = "on"

    def close(self):
        """
        Turn off the water pump relay on.

        Args:
            No args.

        Returns:
            No return.
        """
        self.valve.off()
        self.status = "off"
