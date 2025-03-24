from machine import Pin
from hx711 import HX711
import time
import network
import urequests as requests

# Wi-Fi 
SSID = "ifone"
PASSWORD = "Inder2003"

# initialize HX711 pins
dout = 4  # DAT
pd_sck = 5  # CLK

# load calibration values (replace with your values)
tare_offset = -82530  # replace these with Tare Offset value from calibration 
cal_factor = 315.7089  # replace these with Calibration Factor value from calibration

# initialize HX711
hx = HX711(d_out=dout, pd_sck=pd_sck)

# connect to  the Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print("Connecting to Wi-Fi...")
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected to Wi-Fi:", wlan.ifconfig())

# read the weight
def read_weight():
    hx.power_on()
    time.sleep(1)
    hx.channel = HX711.CHANNEL_A_128
    hx.read()  # Perform an initial read to stabilize

    raw_value = hx.read() - tare_offset
    weight = (raw_value / cal_factor) / 1000 
    return weight

try:
    connect_to_wifi()
    hx.power_on()
    time.sleep(1)
    hx.channel = HX711.CHANNEL_A_128
    hx.read()  # initial stabilization

    while True:
        weight = read_weight()
        print(f"Weight: {weight:.2f} kg")
        time.sleep(1)  # send data 
except KeyboardInterrupt:
    print("Program stopped.")
    hx.power_off()