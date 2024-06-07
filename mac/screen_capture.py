import psutil
import numpy as np
from Quartz.CoreGraphics import (
    CGWindowListCopyWindowInfo, kCGWindowListOptionAll, kCGNullWindowID, 
    CGWindowListCreateImage, kCGWindowImageDefault, CGRectNull,
    kCGWindowListOptionIncludingWindow
)
import Quartz.ImageIO as CGImage

# Function to get all Chrome processes
def get_chrome_processes():
    chrome_processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        if 'chrome' in proc.info['name'].lower():
            chrome_processes.append(proc.info)
    return chrome_processes

# Function to select the correct Chrome process
def select_chrome_process():
    chrome_processes = get_chrome_processes()
    # print("List of Chrome processes:")
    # for index, proc in enumerate(chrome_processes):
    #     print(f"{index}: PID={proc['pid']}, Name={proc['name']}")
    # Select the last Google Chrome process
    for proc in reversed(chrome_processes):
        if proc['name'] == 'Google Chrome':
            return proc['pid']
    return None

# Function to get the window ID of the Chrome process
def get_window_id(pid):
    window_list = CGWindowListCopyWindowInfo(kCGWindowListOptionAll, kCGNullWindowID)
    for window in window_list:
        if window['kCGWindowOwnerPID'] == pid and 'kCGWindowName' in window and window['kCGWindowName']:
            return window['kCGWindowNumber']
    return None

# Function to capture the screen of the specified window
def capture_window(window_id):
    image = CGWindowListCreateImage(CGRectNull, kCGWindowListOptionIncludingWindow, window_id, kCGWindowImageDefault)
    if image is None:
        print("Unable to capture window image")
        return None
    width = CGImage.CGImageGetWidth(image)
    height = CGImage.CGImageGetHeight(image)
    data = CGImage.CGDataProviderCopyData(CGImage.CGImageGetDataProvider(image))
    buffer = np.frombuffer(data, dtype=np.uint8)
    if buffer.size != width * height * 4:
        print(f"Buffer size does not match the expected size: {buffer.size} != {width * height * 4}")
        return None
    buffer = buffer.reshape((height, width, 4))
    return buffer
