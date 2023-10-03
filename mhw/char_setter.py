from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from time import sleep

keyboard = KeyboardController()
mouse = MouseController()

if __name__ == "__main__":
    # tap f13 after 10 seconds
    # sleep(10)
    # keyboard.tap(Key.f13)
    # press mouse button 3 after 20 seconds
    sleep(5)
    mouse.press(Button.x1)
    mouse.press(Button.x2)
    sleep(0.1)
    mouse.release(Button.x1)
    mouse.release(Button.x2)
