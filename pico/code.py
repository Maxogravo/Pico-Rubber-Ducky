import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import os,json

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

filepath = os.getcwd() + "/pico_conf.json"

with open(filepath, 'r') as f:
    data = f.read()
    data = json.loads(data)
    instruction = data.get("instruction")
    osv = data.get("os")
    
if osv == "win":
    kbd.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.3)
elif osv == "mac":
    kbd.send(Keycode.COMMAND, Keycode.SPACE)
    word = "Terminal"
    time.sleep(0.1)
    layout.write("terminal")
    time.sleep(0.3)
    kbd.send(Keycode.ENTER)
    time.sleep(0.1)
else:
    kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)
    time.sleep(0.3)

layout.write(instruction)
kbd.send(Keycode.ENTER)