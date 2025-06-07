from pynput import keyboard
from pynput.keyboard import Key
import threading
import pyperclip
from time import sleep
from sys import exit

delay = None
code = []

def launch():
    print("~Welcome to CodePaster!~")
    sleep(0.1)
    print("Please COPY your code")
    sleep(0.2)
    input("Press Enter when done...")
    code = pyperclip.paste().splitlines()
    if not code:
        print("No code detected. Please copy your code to the clipboard and try again.")
        return []
    else:
        sleep(0.1)
        print("Code detected:")
    print("--------------------------------------------------")
    sleep(0.3)
    print(code)
    sleep(0.1)
    print("--------------------------------------------------")
    return code

code = launch()
sleep(0.1)
print("Please enter a delay between each key press (in milliseconds): ")
sleep(0.3)
delay = float(input("Delay: "))
sleep(0.1)
print("--------------------------------------------------")
sleep(0.3)
print("Delay set to: " + str(delay) + " milliseconds")
sleep(0.1)
print("---------------------------------------------------")
sleep(0.2)

pressed_keys = {}

def on_press(key):
    if key == Key.alt_l and pressed_keys.get(Key.f11, False):
        threading.Thread(target=Paste_Code).start()

def on_release(key):  # This function is called when a key is released
    if key in pressed_keys:
        pressed_keys[key] = False  # to indicate the key is no longer pressed

def stopcode():
    print("Stopping...")
    exit()

def Paste_Code():
    keyboard_controller = keyboard.Controller()
    sleep(1)
    for line in code:
        for char in line:
            keyboard_controller.press(char)
            keyboard_controller.release(char)
            sleep(delay / 1000)  # Convert milliseconds to seconds
        keyboard_controller.press(Key.enter)
        keyboard_controller.release(Key.enter)
    print("Pasting code...")

def on_key_event(key):
    if key == Key.alt_l:
        pressed_keys[Key.alt_l] = True
    if key == Key.f11:
        pressed_keys[Key.f11] = True
        if pressed_keys.get(Key.alt_l, False):
            on_press(Key.alt_l)
    if key == Key.f12:
        stopcode()

listener = keyboard.Listener(
    on_press=on_key_event,
    on_release=on_release
)  # This creates a listener that will call the on_press and on_release functions when keys are pressed or released

listener.start()
print("Running..\n you can now minimize this window.")
print("Press left Alt + F11 to start. Press F12 to stop.")
listener.join()