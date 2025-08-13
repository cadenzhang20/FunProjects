import pyautogui
from time import sleep
from datetime import datetime

log_file_path = "/macros/p2_mouse_tracker/log.txt"

log = open(log_file_path, "a")


def session_start():
    time = datetime.now()
    time_frame = time.strftime("Session at %-I:%M %p --- %Y/%m/%d")
    log.write(time_frame + "\n")
    log.write("-" * len(time_frame) + "\n")
    log.flush()


session_start()

while True:
    user_choice = input("tracker.py: ")

    if user_choice == "clear logs":
        if input("Are you sure? [YES] to confirm: ") == "YES":
            log.close()
            log = open(log_file_path, "w")
            session_start()

    elif user_choice == "q":
        log.write("  :: SESSION ENDED ::  \n")
        break

    elif user_choice == "t":
        user_specs = input(".track time-amount-name: ")

        track_time, amount, t_name = user_specs.split()
        track_time, amount = float(track_time), int(amount)

        print("tracking" + "." * amount, end="")

        log.write(f"  X     | Y        ;{t_name}\n")

        last_track_x, last_track_y = -1, -1
        wait_time = track_time / amount
        for _ in range(amount):
            mouse_x, mouse_y = pyautogui.position()

            if mouse_x == last_track_x and mouse_y == last_track_y:
                log.write(f"  {mouse_x:0>4}  |  {mouse_y:0>3}   <|--- held\n")
            else:
                log.write(f"  {mouse_x:0>4}  |  {mouse_y:0>3}   \n")

            last_track_x, last_track_y = mouse_x, mouse_y

            print("\b", end="")
            sleep(wait_time)

        print("\rtracked" + " " * amount)
        log.write("\n")
        log.flush()

    else:
        log.write(f"  # {user_choice}\n")
        log.flush()

log.write("\n")
log.close()
