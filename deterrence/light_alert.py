import time
import threading
import os
import platform

def flash_terminal():
    for _ in range(3):
        print("\033[5m[!!!] DRONE DETECTED [!!!]\033[0m")
        time.sleep(0.5)

def blink_screen():
    if platform.system() == "Darwin":
        os.system('osascript -e \'tell app "System Events" to flash screen\'')
    else:
        print("[!] Screen flash not supported on this OS.")

def trigger_light_alert():
    flash_terminal()
    blink_screen()

def alert_async():
    t = threading.Thread(target=trigger_light_alert)
    t.start()
