from pynput.keyboard import Key, Controller, Listener
from time import sleep

keyboard = Controller()

playing_script = False

def on_press(key):
    if key == Key.f6:
        global playing_script
        if playing_script:
            playing_script = False
            return False
        else:
            playing_script = True
            start_script()

def on_release(key):
    return True

def start_script():
    print("Script started.")
    while playing_script:
        keyboard.tap(Key.enter)
        sleep(5.0)
        keyboard.press('w')
        sleep(30)
        keyboard.release('w')
        sleep(0.4)
        keyboard.tap('x')
        sleep(0.4)
        keyboard.tap(Key.enter)
        sleep(6.5)

if __name__ == "__main__":
    print("Press F6 to start the script.")

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
        