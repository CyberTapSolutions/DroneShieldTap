# 🛰️ DroneShieldTap

**DroneShieldTap** is an open-source drone detection and deterrence toolkit built for cybersecurity professionals and ethical hackers. It detects nearby drones using Wi-Fi MAC address fingerprinting and provides deterrent mechanisms such as sound alerts and visual flashing.

> ⚠️ This tool is for **educational and research purposes only**. Unauthorized signal interference is illegal in many jurisdictions.

---

## 🔧 Features

- 🚁 **Wi-Fi Drone Detection** (DJI, Parrot, Yuneec, Autel, etc.)
- 🔊 **Sound Alert System** (plays an MP3 siren)
- 💡 **Light Flash Alert** (terminal and screen flashes)
- 📝 **Event Logging** to `drone_detections.log`
- 🧪 Menu-based launcher via `main.py`

---

## 📁 Project Structure

```
DroneShieldTap/
├── detection/
│   └── wifi_scanner.py        # Wi-Fi sniffing for drone MACs
├── deterrence/
│   ├── light_alert.py         # Flash screen/terminal alert
│   ├── sound_emitter.py       # Play alert sound
│   └── notifier.py            # Placeholder for future alerts (email/Discord)
├── utils/
│   └── logger.py              # Logs drone detections
├── main.py                    # Main menu launcher
├── requirements.txt           # Python dependencies
├── README.md                  # Project overview
└── LICENSE                    # MIT License
```
