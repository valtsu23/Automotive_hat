import time
import adafruit_pixelbuf
import board
from adafruit_raspberry_pi5_neopixel_write import neopixel_write

NEOPIXEL = board.D13
num_pixels = 8

class Pi5Pixelbuf(adafruit_pixelbuf.PixelBuf):
    def __init__(self, pin, size, **kwargs):
        self._pin = pin
        super().__init__(size=size, **kwargs)

    def _transmit(self, buf):
        neopixel_write(self._pin, buf)

pixels = Pi5Pixelbuf(board.D21, num_pixels, auto_write=True, byteorder="BGR")
colors = ((255, 0, 0), (0, 255, 0), (0, 0, 255))

try:
    while True:
        for x in range(3):
            color = colors[x]
            for x in range(8):
                pixels[x] = color
                time.sleep(.1)
                pixels[x] = (0, 0, 0)

except KeyboardInterrupt:
    pixels.fill((0, 0, 0))