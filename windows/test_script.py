import subprocess
import psutil

# Get the PID of the Chrome process running Bonk.io
def get_chrome_pid():
    for proc in psutil.process_iter(['pid', 'name']):
        if 'Google Chrome' in proc.info['name']:
            return proc.pid
    return None

chrome_pid = get_chrome_pid()
if chrome_pid is None:
    print("Chrome process not found")
    exit()
print(f"Chrome PID: {chrome_pid}")

# Keycode mappings for macOS
key_mapping = {
    'up': 126,
    'down': 125,
    'left': 123,
    'right': 124
}

def press_key(key):
    key_code = key_mapping.get(key)
    if key_code is not None:
        print(f"Pressing key {key} (code {key_code}) to PID {chrome_pid}")
        subprocess.run(["./sendkeys", str(chrome_pid), str(key_code), "true"])
        subprocess.run(["./sendkeys", str(chrome_pid), str(key_code), "false"])

# Test pressing the "up" key
press_key('up')
