from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller as MouseController
from time import sleep

mouse = MouseController()

def on_press(key):
    if key == Key.f13:
        mouse.press(Button.x1)
        mouse.press(Button.x2)
        sleep(0.1)
        mouse.release(Button.x1)
        mouse.release(Button.x2)

def on_release(key):
    return True

if __name__ == "__main__":
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
