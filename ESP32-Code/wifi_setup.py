""""Conncting to the WIFI getway"""

import network
import time
from config import WIFI_PASSWORD, WIFI_SSID

# Echo connecting start
print("Connecting to WiFi", end="")

# Init the stander interface
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

# Set the WIFI info
sta_if.connect(
    WIFI_SSID,
    WIFI_PASSWORD
)

# A connection loop
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)

print(" Connected!")
