import os

def print_menu():
    print("\n🔧 DroneShieldTap Toolkit Menu")
    print("1. Start Wi-Fi Drone Scanner")
    print("2. Play Sound Alert (Test)")
    print("3. Flash Light Alert (Test)")
    print("4. Exit")

def main():
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
