# Automotive hat for Raspberry Pi

### To do:
- Add pictures

### Additional files
- [Schematic](https://www.dropbox.com/scl/fi/iavjqscsv059lmrkn0drn/Automotive_hat_Schematics.pdf?rlkey=1wznfggolzi144akhuucwucm8&st=d3ek3ai6&dl=0)
- [Libre PCB project](https://www.dropbox.com/scl/fi/lksvlw7bsu9jo7t3yq4of/Automotive_hat.lppz?rlkey=w2fywejnwz0x9pa1phe22ul6w&st=q8x242gr&dl=0)
- [Step file](https://www.dropbox.com/scl/fi/zjf9aknypds8e6wfc7z42/Automotive_hat.step?rlkey=rbrz324ngjgzv7312mqohl4mg&st=4p1kkjih&dl=0)
- [3D model viewer](https://3dviewer.net/#model=https://www.dropbox.com/scl/fi/zjf9aknypds8e6wfc7z42/Automotive_hat.step?rlkey=rbrz324ngjgzv7312mqohl4mg&st=urt7w919&dl=0)

This project was inspired by my earlier project: [DIY-Emu-Black-Dash-Rpi5-V2](https://github.com/valtsu23/DIY-Emu-Black-Dash-Rpi5-V2).
When I tried to find similar products I only found CarPiHAT by ThePiHut, but it lacked analog inputs and has pretty low number of IO:s. 

### Main features: 
- Automatic power on and shutdown is possible. After shutdown Rpi won't use any power. 
- Fail safe button to cut the power, if normal shutdown cannot be done
- 12V to 5V 3,4A DC-DC converter (Pololu D30V30F5)
- Can Bus (MCP2515 controller)
- One Neopixel output with voltage level converter
- 5 analog inputs 0-5V with a place for pull up resistors (MCP3008 ADC)
- 4 Digital inputs 12V tolerant (ACPL-247-560E Optocoupler)
- 4 Digital low side outputs. 12V 500mA tolerant with flyback diodes (ULN2803AD Darlington driver)
- Stemma QT connector for i2c devices
- 5V power output for display etc. 

### 12V power inputs:
- Constant power from battery
- Switched power (usually from ignition switch)

### How power circuit works:
Switched 12V power wakes up the device and Raspberry Pi starts booting and on boot process the relay turns on. Shutdown command can be given from software or Digital input 1 can be used to trigger shutdown when switched power is lost. On Pcb there is a solder jumper named SW to connect switched power to Digital input 1. For this function a dtoverlay must be added to config.txt. After safe shutdown the relay turns off and cuts power from the device. 

### Wiring
- I recommend using 0.5mm2 wires for power and ground. 
- If you use Digital outputs I recommend using extra ground wire to J2 pin 1. 

### Connectors J1 - J3
- Connectors are designed to use screw terminal: Pheonix contact 1725711
- Normal .1" pin header can be used 
- 0.5mm2 wires can be soldered directly, but it's a tight fit

### Pin out J1 from right to left:
1. Constant 12V (usually from battery)
2. Switched 12V (usually from ignition switch)
3. GND to chassis ground
4. Can Bus High
5. Can Bus Low
6. 5V output for Neopixel
7. Neopixel digital output (GPIO 21)
8. GND for Neopixel

### Pin out J2 from right to left:
1. GND to chassis ground (Extra ground if 12V Digital ouputs are used)
2. Analog sensor ground 
3. Analog input 5
4. Analog input 4
5. Analog input 3
6. Analog input 2
7. Analog input 1
8. 5V output for analog sensors

### Pin out J3 from right to left:
1. 12V Digital output 4 (switch to ground) GPIO 23
2. 12V Digital output 3 (switch to ground) GPIO 18
3. 12V Digital output 2 (switch to ground) GPIO 16
4. 12V Digital output 1 (switch to ground) GPIO 12
5. Digital input 4 (12V tolerant) GPIO 19
6. Digital input 3 (12V tolerant) GPIO 13
7. Digital input 2 (12V tolerant) GPIO 6
8. Digital input 1 (12V tolerant) GPIO 5

### Add these lines to /boot/firmware/config.txt for hardware support:
- To activate the power relay `dtoverlay=gpio-poweroff,active_low=1,inactive_delay_ms=0,gpiopin=22`
- Can Bus chip `dtoverlay=mcp2515-can1,oscillator=16000000,interrupt=25`
- DIN 1 automatic shutdown, when switched 12v is lost. Add this line only if solder jumper SW on the pcb is connected! `dtoverlay=gpio-shutdown,gpio_pin=5,active_low=0`

### How to run examples in Raspberry Pi OS and OS Lite
- First create a Python Virtual Environment, by following [this guide](https://learn.adafruit.com/python-virtual-environment-usage-on-raspberry-pi/overview)
Remember to include system site packages!
- For Can Bus support install python-can `pip install python-can`
- For Neopixels install Adafruit-Blinka `pip install Adafruit-Blinka`
- For Neopixels on Raspberry Pi 5 also `pip install Adafruit-Blinka-Raspberry-Pi5-Neopixel`
