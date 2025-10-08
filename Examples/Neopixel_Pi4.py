import board
import neopixel
import time

num_pixels = 8

pixels = neopixel.NeoPixel(board.D21, num_pixels)
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
