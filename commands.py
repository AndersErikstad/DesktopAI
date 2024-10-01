from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key
from PIL import ImageGrab
import time

mouse = MouseController()
keyboard = KeyboardController()

def move(x, y):
    """Move the mouse to the specified coordinates."""
    mouse.position = (int(x), int(y))

def left_click():
    """Perform a left mouse click."""
    mouse.click(Button.left, 1)

def right_click():
    """Perform a right mouse click."""
    mouse.click(Button.right, 1)

def drag_drop(x1, y1, x2, y2):
    """Drag from (x1, y1) to (x2, y2)."""
    mouse.position = (int(x1), int(y1))
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.position = (int(x2), int(y2))
    time.sleep(0.1)
    mouse.release(Button.left)

def type_text(text):
    """Type the given text."""
    keyboard.type(text)

def key_press(key):
    """Press a keyboard key."""
    key = get_key(key)
    keyboard.press(key)

def key_release(key):
    """Release a keyboard key."""
    key = get_key(key)
    keyboard.release(key)

def screenshot(filename='screenshot.png'):
    """Take a screenshot and save it."""
    image = ImageGrab.grab()
    image.save(filename)

def get_key(key_str):
    """Convert string to pynput Key object if necessary."""
    special_keys = {
        'alt': Key.alt,
        'alt_l': Key.alt_l,
        'alt_r': Key.alt_r,
        'backspace': Key.backspace,
        'caps_lock': Key.caps_lock,
        'cmd': Key.cmd,
        'cmd_r': Key.cmd_r,
        'ctrl': Key.ctrl,
        'ctrl_l': Key.ctrl_l,
        'ctrl_r': Key.ctrl_r,
        'delete': Key.delete,
        'down': Key.down,
        'end': Key.end,
        'enter': Key.enter,
        'esc': Key.esc,
        'f1': Key.f1,
        'f2': Key.f2,
        'f3': Key.f3,
        'f4': Key.f4,
        'f5': Key.f5,
        'f6': Key.f6,
        'f7': Key.f7,
        'f8': Key.f8,
        'f9': Key.f9,
        'f10': Key.f10,
        'f11': Key.f11,
        'f12': Key.f12,
        'home': Key.home,
        'insert': Key.insert,
        'left': Key.left,
        'page_down': Key.page_down,
        'page_up': Key.page_up,
        'right': Key.right,
        'shift': Key.shift,
        'shift_l': Key.shift_l,
        'shift_r': Key.shift_r,
        'space': Key.space,
        'tab': Key.tab,
        'up': Key.up,
    }
    return special_keys.get(key_str.lower(), key_str)
