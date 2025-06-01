from scapy.all import sniff, Dot11
from utils.logger import log_event
from deterrence.sound_emitter import alert_async as sound_alert
from deterrence.light_alert import alert_async as light_alert

DRONE_OUI_PREFIXES = {
    "60:60:1F": "DJI",
    "90:3A:E6": "Parrot",
    "A0:14:3D": "DJI",
    "00:26:7E": "3D Robotics",
    "14:FE:34": "Yuneec",
    "7C:70:BC": "Autel Robotics"
}

def is_drone(mac):
    prefix = mac.upper()[0:8]
    return DRONE_OUI_PREFIXES.get(prefix)

def packet_handler(pkt):
    if pkt.haslayer(Dot11):
        mac = pkt.addr2
        if mac:
            drone_brand = is_drone(mac)
            if drone_brand:
                log_event(f"🚁 Drone Detected - Brand: {drone_brand}, MAC: {mac}")
                print(f"[!] Drone Detected: {drone_brand} | MAC: {mac}")
                sound_alert()
                light_alert()

def start_sniff(interface):
    print(f"[*] Scanning on interface: {interface}")
    sniff(iface=interface, prn=packet_handler, store=0)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: sudo python3 wifi_scanner.py <interface>")
    else:
        start_sniff(sys.argv[1])
