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
    def __init__(self, pin):
        """
        Initializes a new instance of the Pump class.
        Attributes:
            Pin(int) : Un integer pin number.
        """
        # Set the pin mode (output)
        self.valve = Pin(pin, Pin.OUT)
        # Init the pin with off state(0)
        self.valve.off()

    def open(self):
        """
        Turn on the water pump relay on.

        Args:
            No args.

        Returns:
            No return.
        """
        self.valve.on()

    def close(self):
        """
        Turn off the water pump relay on.

        Args:
            No args.

        Returns:
            No return.
        """
        self.valve.off()
