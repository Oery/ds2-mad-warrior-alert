import psutil
import os
import time
import sys
import threading
import playsound

PROCESS_NAME = "DarkSoulsII.exe"  # Process name to monitor
REFRESH_RATE = 0.5  # Refresh rate in seconds
THRESHOLD = 5  # Memory spike threshold in MB
SOUND_ALERT_ENABLED = True  # Enable or disable the sound alert
ALERT_PATH = "./mad_warrior_alert.mp3"  # Path to the alert sound file

def play_alert_sound():
    """Play a sound to alert the user of a memory spike."""
    try:
        if SOUND_ALERT_ENABLED: playsound.playsound(ALERT_PATH)
    except Exception as e:
        pass
        
def clear_console():
    """Clear the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_memory_usage(process):
    """Get memory usage of a process."""
    try:
        memory_usage = process.memory_info().rss / 1024 ** 2  # Convert bytes to MB
        return memory_usage
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        print(f"Process {process.name()} no longer exists.")
        sys.exit(1)
        
def find_process_by_name(process_name):
    """Find a process by its name."""
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] == process_name:
            return proc
    return None

def monitor_memory_usage():
    """Monitor the memory usage and display a message if there's a spike."""
    
    process = None
    while process is None:
        process = find_process_by_name(PROCESS_NAME)
        if process is None:
            clear_console()
            print(f"Waiting for process {PROCESS_NAME} to start...")
            time.sleep(1)  # Wait a bit before trying again
        else:
            clear_console()
            print(f"Found process {PROCESS_NAME}, starting memory usage monitoring.")
            time.sleep(1)  # Wait a bit before starting the monitoring
    
    prev_memory_usage = get_memory_usage(process)
    spike_message_displayed_until = 0 # Timestamp until which the alert is displayed
    
    while True:
        current_time = time.time()
        current_memory_usage = get_memory_usage(process)
        
        current_memory_usage_int = int(current_memory_usage) # Convert to an integer for display
        
        if current_time < spike_message_displayed_until:
            clear_console()
            print(f"Current Memory Usage: {current_memory_usage_int} Mo")
            print("/!\ Mad Warrior Detected /!\\")
            threading.Thread(target=play_alert_sound, daemon=True).start()
            time.sleep(5)
        elif current_memory_usage != prev_memory_usage:
            clear_console()
            print(f"Current Memory Usage: {current_memory_usage_int} Mo")
            
        if current_memory_usage - prev_memory_usage > THRESHOLD:
            spike_message_displayed_until = current_time + 5  # Set the future timestamp to stop displaying the alert
                
        prev_memory_usage = current_memory_usage
        time.sleep(0.5)  # Refresh rate

if __name__ == "__main__":
    monitor_memory_usage()
