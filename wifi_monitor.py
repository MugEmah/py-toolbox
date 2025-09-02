import subprocess
import platform
import time
import os
from rich.progress import Progress

def get_wifi_strength():
    system = platform.system()
    
    try:
        if system == "Linux":
            #nmcli works on Network Manager-based Linux systems
            result = subprocess.check_output(
                ["nmcli", "-t", "-f", "IN-USE,SSID,SIGNAL", "dev", "wifi"], text=True
                )
            for line in result.splitlines():
                if line.startswith('yes'): #connected network
                    parts = line.split(":")
                    ssid = parts[1]
                    signal = int(parts[2])
                    return ssid, signal
                
        elif system == "Windows":
            result = subprocess.check_output(
                ["netsh", "wlan", "show", "interfaces"], text=True
                )
            ssid, signal = None, None
            for line in result.splitlines():
                if "SSID" in line and "BSSID" not in line:
                    ssid = line.split(":")[1].strip()
                if "Signal" in line:
                    signal = int(line.split(":")[1].strip().replace("%", ""))
            return ssid, signal
        
        elif system == "Darwin": #Mac
            result = subprocess.check_output(
                ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airpot", "-I"], text=True
                )
            ssid, rssi = None, None
            for line in result.splitlines():
                if "SSID:" in line:
                    ssid = line.split(":")[1].strip()
                if "agrCtlRSSI" in line:
                    rssi = int(line.split(":")[1].strip()) #in dBm (negative value)
                if rssi:
                    #convert RSSI dBm to approximate % signal
                    signal = min(max(2 * (rssi + 100), 0), 100)
                    return ssid, signal
        else:
            return None, None
            
    except Exception as e:
        return None, None
    
def monitor(interval=2):
    while True:
        os.system('clear' if platform.system() == "Linux" else "cls")
        ssid, signal = get_wifi_strength()
        if ssid and signal is not None:
            print(f"Connected to: {ssid}")
            print(f"Signal Strength : {signal}%")
            
            #Fancy progress bar
            with Progress() as progress:
                task = progress.add_task("Signal", total=100)
                progress.update(task, completed=signal)
                time.sleep(1) # so bar shows before clearing
                
        else:
            print("Not connected to Wi-Fi")
        time.sleep(interval)
        
if __name__ == "__main__":
    monitor()
    
                
                
                
                
    
    
    
    
    
    
    
    
