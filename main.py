import os

def print_banner():
    banner = r"""
 ____                         ____  _     _      _     _ 
|  _ \ _ __ ___  _ __   ___  / ___|| |__ (_) ___| | __| |
| | | | '__/ _ \| '_ \ / _ \ \___ \| '_ \| |/ _ \ |/ _` |
| |_| | | | (_) | | | |  __/  ___) | | | | |  __/ | (_| |
|____/|_|  \___/|_| |_|\___| |____/|_| |_|_|\___|_|\__,_|
                                                       
                 🛰️ DRONES – Cyber Detection Toolkit
    ─────────────────────────────────────────────────────
    """
    print(banner)

def print_menu():
    print("🔧 DroneShieldTap Toolkit Menu")
    print("1. Start Wi-Fi Drone Scanner")
    print("2. Play Sound Alert (Test)")
    print("3. Flash Light Alert (Test)")
    print("4. Exit")

def main():
    print_banner()
    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            interface = input("Enter monitor-mode interface (e.g., wlan0mon): ")
            os.system(f"sudo python3 detection/wifi_scanner.py {interface}")
        elif choice == "2":
            from deterrence.sound_emitter import alert_async
            alert_async()
        elif choice == "3":
            from deterrence.light_alert import alert_async
            alert_async()
        elif choice == "4":
            print("Exiting DroneShieldTap. Stay safe.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
