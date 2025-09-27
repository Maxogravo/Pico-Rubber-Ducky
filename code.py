import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

def Attack():
    kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)
    time.sleep(1)
    kbd.send(Keycode.F)
    kbd.send(Keycode.A)
    kbd.send(Keycode.S)
    kbd.send(Keycode.T)
    kbd.send(Keycode.F)
    kbd.send(Keycode.E)
    kbd.send(Keycode.T)
    kbd.send(Keycode.C)
    kbd.send(Keycode.H)
    kbd.send(Keycode.ENTER)

Attack()
