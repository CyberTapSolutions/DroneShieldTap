from playsound import playsound
import threading

def play_alert():
    try:
        playsound('alert.mp3')  # Place alert.mp3 in project root
    except Exception as e:
        print(f"[!] Error playing sound: {e}")

def alert_async():
    t = threading.Thread(target=play_alert)
    t.start()
