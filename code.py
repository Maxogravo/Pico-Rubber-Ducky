import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
instruction = input("Enter Instruction: ")

for char in instruction:
    char = "Keycode." + char.upper()
    kbd.send(char)

kbd.send(Keycode.ENTER)
