from hx711 import HX711
from machine import Pin
from utime import sleep

# Define pins for HX711
dout = 4  # Data output pin (DT)
pd_sck = 5  # Clock pin (SCK)

# Initialize HX711
hx = HX711(d_out=dout, pd_sck=pd_sck)

# Calibration process
def calibrate():
    print("Initializing HX711...")
    hx.power_on()
    sleep(1)
    print("Taring the scale...")
    hx.channel = HX711.CHANNEL_A_128
    hx.read()  # Perform an initial read to stabilize
    tare_offset = hx.read()
    print(f"Tare Offset: {tare_offset}")

    print("Place a known weight on the scale...")
    input("Press Enter when the weight is placed...")

    known_weight = float(input("Enter the weight in grams of the known mass: "))
    raw_value = hx.read()
    print(f"Raw Value for Known Weight: {raw_value}")
    
    calibration_factor = raw_value / known_weight
    print(f"Calibration Complete. Calibration Factor: {calibration_factor}")

    return tare_offset, calibration_factor

# Run calibration
tare_offset, cal_factor = calibrate()

# Save these values for the weight reading script
print(f"Save these values for the next script: Tare Offset = {tare_offset}, Calibration Factor = {cal_factor}")

hx.power_off()

