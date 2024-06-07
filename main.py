import time
import psutil
import cv2
import numpy as np
import decision_logic  # Import the decision logic functions
from screen_capture import capture_window, get_chrome_processes, select_chrome_process, get_window_id

# Initialize
chrome_pid = select_chrome_process()
if chrome_pid is None:
    print("Chrome process not found")
    exit()

print(f"Selected Chrome PID: {chrome_pid}")

window_id = get_window_id(chrome_pid)
if window_id is None:
    print("Window ID not found for the given Chrome process")
    exit()

print(f"Selected Window ID: {window_id}")

# Capture the initial frame
initial_screen = capture_window(window_id)
initial_screen_resized = cv2.resize(initial_screen, (640, 360))
initial_gray = cv2.cvtColor(initial_screen_resized, cv2.COLOR_BGRA2GRAY)

# Process a single frame for debugging
try:
    current_screen = capture_window(window_id)  # Capture the window screen
    if current_screen is not None:
        current_screen_resized = cv2.resize(current_screen, (640, 360))
        current_bgr = cv2.cvtColor(current_screen_resized, cv2.COLOR_BGRA2BGR)
        player_pos, direction = decision_logic.find_player_position(initial_gray, current_bgr)
        screen_with_player = decision_logic.draw_player_position(current_bgr, player_pos)
        
        # Display results
        cv2.imshow("Player and Obstacles Detection", screen_with_player)
        
        if cv2.waitKey(0) & 0xFF == ord('q'):  # Allow exiting the loop with 'q'
            pass
finally:
    cv2.destroyAllWindows()  # Close all OpenCV windows
