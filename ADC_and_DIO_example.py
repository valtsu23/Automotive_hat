import gpiozero
import time

# MCP3008 Analog to digital converter channels 1-5
adc_1 = gpiozero.MCP3008(1)
adc_2 = gpiozero.MCP3008(2)
adc_3 = gpiozero.MCP3008(3)
adc_4 = gpiozero.MCP3008(4)
adc_5 = gpiozero.MCP3008(5)

# 12V tolerant digital inputs channels 1-4.
# Pull up resistors on pcb, so reversed signal with active_state=False
din_1 = gpiozero.InputDevice(pin=5, pull_up=None, active_state=False)
din_2 = gpiozero.InputDevice(pin=6, pull_up=None, active_state=False)
din_3 = gpiozero.InputDevice(pin=13, pull_up=None, active_state=False)
din_4 = gpiozero.InputDevice(pin=19, pull_up=None, active_state=False)

# 12V tolerant output (provides the ground)
dout_1 = gpiozero.OutputDevice(pin=12)
dout_2 = gpiozero.OutputDevice(pin=16)
dout_3 = gpiozero.OutputDevice(pin=18)
dout_4 = gpiozero.OutputDevice(pin=23)

while True:
    print("Adc channel 1: ", adc_1.raw_value)
    print("Adc channel 2: ", adc_2.raw_value)
    print("Adc channel 3: ", adc_3.raw_value)
    print("Adc channel 4: ", adc_4.raw_value)

    print("DIN 1 state:", din_1.is_active)
    print("DIN 2 state:", din_2.is_active)
    print("DIN 3 state:", din_3.is_active)
    print("DIN 4 state:", din_4.is_active)
    time.sleep(1)

    dout_1.on()
    time.sleep(1)
    dout_1.off()
    time.sleep(1)

    dout_2.on()
    time.sleep(1)
    dout_2.off()
    time.sleep(1)

    dout_3.on()
    time.sleep(1)
    dout_3.off()
    time.sleep(1)

    dout_4.on()
    time.sleep(1)
    dout_4.off()
    time.sleep(1)
