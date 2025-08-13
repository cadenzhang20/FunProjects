import pyautogui
from pynput.keyboard import Listener

number_mode = False

if not number_mode:
    [print(x) for x in ["r", "i", "n", "v"]]


def key_press(key):
    key = str(key).strip("'")

    if key == "Key.esc":
        return False

    if number_mode and key.isdigit():
        key = int(key)
        if key == 1:
            # top left
            pyautogui.click(352, 381)
        elif key == 2:
            # top right
            pyautogui.click(1062, 367)
        elif key == 3:
            # bottom right
            pyautogui.click(1028, 693)
        elif key == 4:
            # bottom left
            pyautogui.click(331, 699)

    else:
        if key == "r":
            # top left
            pyautogui.click(352, 381)
        elif key == "i":
            # top right
            pyautogui.click(1062, 367)
        elif key == "n":
            # bottom right
            pyautogui.click(1028, 693)
        elif key == "v":
            # bottom left
            pyautogui.click(331, 699)


with Listener(on_press=key_press) as li:
    li.join()
