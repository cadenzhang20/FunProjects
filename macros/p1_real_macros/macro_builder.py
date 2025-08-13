import pyautogui
from time import sleep
from pynput.keyboard import Listener
from threading import Thread

# width = 1440px; height = 900px;


def mac_hotkey(*args):
    for a in args:
        pyautogui.keyDown(a)
    sleep(0)
    for a in args:
        pyautogui.keyUp(a)


# The different function of the macro
def open_tabs():
    first_page = "https://racing.blooket.com/host/settings?gid=65c8057ee948152636b98393"
    second_page = "https://play.blooket.com/play"

    # access first page
    pyautogui.click(160, 90)
    pyautogui.typewrite(first_page)
    pyautogui.press('enter')

    # create the game
    pyautogui.moveTo(1033, 793)
    sleep(2)
    pyautogui.scroll(-10)
    pyautogui.click()
    pyautogui.write("0")
    pyautogui.click(1069, 563)
    pyautogui.click(722, 308)

    # create second page
    mac_hotkey('command', 't')
    pyautogui.typewrite(second_page)
    pyautogui.press('enter')


def format_tabs():
    # drag the second tab halfway down
    pyautogui.moveTo(430, 50)
    pyautogui.drag(0, 450, button='left')

    # minimize that half dragged tab to the right side
    pyautogui.moveTo(0, 700)
    pyautogui.drag(1000, button='left')

    pyautogui.click(1086, 750)
    sleep(0.1)
    pyautogui.click(None, None)


def start_game():
    # enter game id
    pyautogui.click(971, 212, button="right")
    pyautogui.click(972, 260)
    pyautogui.click(1086, 810)
    mac_hotkey('command', 'v')
    pyautogui.press('enter')

    # enter nickname (random)
    sleep(1.5)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.click(1120, 381)
    sleep(0.1)
    pyautogui.click(None, None)

    # press okay
    sleep(7)
    pyautogui.click(1128, 785)
    sleep(0.1)
    pyautogui.click(None, None)


def game_loop():
    global pos_x, pos_y

    while is_clicking:
        pyautogui.click(pos_x, pos_y)
        sleep(0.1)


def reset_macro():
    pyautogui.click(1229, 802)
    pyautogui.click(1342, 578)
    pyautogui.click(615, 603)
    sleep(0.1)
    pyautogui.click(None, None)


def full_macro():
    global is_clicking
    global full_macro_running

    open_tabs()
    format_tabs()
    while full_macro_running:
        start_game()

        count = 0
        while count < 300 and full_macro_running:
            pyautogui.click(1128, 870)
            sleep(0.1)
            count += 1

        sleep(12)

        reset_macro()

        sleep(2)


alt_char_dict = {'¡': 1, '™': 2, '£': 3, '¢': 4, '∞': 5, '§': 6, '¶': 7, '•': 8, 'ª': 9, 'º': 0}
alt_pressed = False
is_clicking = False
full_macro_running = False
pos_x, pos_y = 0, 0


# The key press functions of the macro
def key_press(key):
    global alt_pressed
    global is_clicking
    global full_macro_running

    global pos_x, pos_y

    key = str(key).strip("'")
    if key == "Key.esc":
        return False

    elif key == "Key.alt_r":
        alt_pressed = True

    elif alt_pressed:
        if key in alt_char_dict:
            key = alt_char_dict[key]

            if key == 1:
                sleep(0.3)
                open_tabs()
                format_tabs()
            elif key == 2:
                start_game()
            elif key == 3:
                if not is_clicking:
                    is_clicking = True
                    pos_x, pos_y = 1128, 870
                    button_clicker = Thread(target=game_loop)
                    button_clicker.start()
                else:
                    is_clicking = False
            elif key == 4:
                sleep(0.3)
                reset_macro()
            elif key == 9:
                if not is_clicking:
                    is_clicking = True
                    pos_x, pos_y = list(pyautogui.position())
                    button_clicker = Thread(target=game_loop)
                    button_clicker.start()
                else:
                    is_clicking = False
            elif key == 0:
                sleep(0.3)
                if not full_macro_running:
                    full_macro_running = True
                    macro = Thread(target=full_macro)
                    macro.start()
                else:
                    full_macro_running = False


def key_release(key):
    global alt_pressed

    key = str(key).strip("'")
    if key == "Key.alt_r":
        alt_pressed = False


with Listener(on_press=key_press, on_release=key_release) as li:
    li.join()
