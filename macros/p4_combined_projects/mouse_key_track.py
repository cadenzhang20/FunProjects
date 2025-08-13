import pyautogui
from datetime import datetime
from pynput.keyboard import Listener

file_loc = "macros/p4_combined_projects/log.txt"
log = open(file_loc, "a")


def session_start():
    time_frame = datetime.now().strftime("Session at %-I:%M %p --- %Y/%m/%d")

    log.write(f"""{time_frame}
{"-" * len(time_frame)}
  """)
    log.flush()


def key_press(key):
    key = str(key).strip("'")
    if key == "Key.esc":  # immediately exits the program if "esc" is pressed
        return False

    if key == "Key.alt_r":
        mouse_pos = list(pyautogui.position())

        # Writes the position to logs, allows user to comment
        log.write(f"[{mouse_pos[0]:0>4}, {mouse_pos[1]:0>3}]: \n    \n  ")
        log.flush()


session_start()
with Listener(on_press=key_press) as li:
    li.join()

log.write(":: SESSION ENDED ::  \n\n")
log.close()
