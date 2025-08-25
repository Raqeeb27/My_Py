from time import sleep
from platform import system, release

try:
    from pyautogui import click, hotkey, press, size
except ImportError:
    print("This script requires the 'pyautogui' module.\nPlease install it using 'pip install pyautogui' and try again.")
    exit(1)


# Get screen width and height
screen_width, screen_height = size()

# Click at the rightmost top safe corner
click(x=screen_width-2, y=1, clicks=1, interval=0, button='left')

hotkey("alt", "f4")
sleep(0.3)
press("up")

# Only press "up" if running on Windows 10
if system() == "Windows" and release() == "10":
    press("up")

sleep(0.3)
press("enter")
