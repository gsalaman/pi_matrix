#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw

def getch():
  import sys, tty, termios
  old_settings = termios.tcgetattr(0)
  new_settings = old_settings[:]
  new_settings[3] &= ~termios.ICANON & ~termios.ECHO
  try:
    termios.tcsetattr(0, termios.TCSANOW, new_settings)
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(0, termios.TCSANOW, old_settings)
  return ch 

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 64
options.cols = 64 
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)

image = Image.new("RGB", (5,5))
draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, 4, 4), fill=(0, 0, 0), outline=(0,0,255))

x = 32
y = 32

matrix.SetImage(image, x, y)

try:
  print("CTL-C to stop.  j=left, l=right, i=up, k=down")
  while True:
    key = getch()
    if key == 'j':
      if x > 0:
        x = x - 1
    if key == 'l':
      if x < 59:
        x = x + 1
    if key == 'i':
      if y > 0:
        y = y - 1;
    if key == 'k':
      if y < 59:
        y = y + 1 

    matrix.Clear()
    matrix.SetImage(image, x, y)

except KeyboardInterrupt:
  sys.exit(0)
