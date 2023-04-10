import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 30)  # Raspberry Pi wiring!
# lightup entire stip gree
pixels.fill((0, 255, 0))
