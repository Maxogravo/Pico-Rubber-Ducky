import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

def Attack():
   instruction = input(“Enter instruction: ”)
   for char in instruction:
      char = “Keycode.” + char
      kbd.send(char)
   kbd.send(Keycode.ENTER)

Attack()
