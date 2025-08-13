import pyautogui
from pynput.keyboard import Listener

key_dict = {}
mode = 0
# mode 0 = press
# mode 1 = listen


def key_press(key):
    global mode

    key = str(key).strip("'")
    if key == "Key.esc":  # immediately exits the program if "esc" is pressed
        return False

    if key == "Key.alt_r":
        mode = 1 - mode
        print("ON") if mode else print("OFF")
        return

    if mode == 0:
        if key in key_dict:
            pyautogui.click(key_dict[key])
    else:
        if key not in key_dict:
            key_dict[key] = pyautogui.position()
        else:
            key_dict.pop(key)


with Listener(on_press=key_press) as li:
    li.join()


