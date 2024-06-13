# import time
# import cv2
# import numpy as np
# import decision_logic  # Import the decision logic functions
# from screen_capture import grabScreen, getWindowHandle, bringWindowToFront
# from new_object_detection import getContours

# # Get the window handle for the bonk.io window
# window_name = 'bonk.io - Official Site: Play Bonk Here! - Google Chrome'
# hwnd = getWindowHandle(window_name)

# # Bring the window to the foreground
# bringWindowToFront(hwnd)

# # Define the region you want to capture (left, top, right, bottom)
# region = (245, 215, 880, 640)  # Adjust these values to the region where the game is actually played


# # img = getContours(frame)
# # cv2.imshow('Contours', img)
# # if cv2.waitKey(1) & 0xFF == ord('q'):  # Allow exiting the loop with 'q'
# #     cv2.destroyAllWindows()
# # current_screen = window_capture.get_screenshot()

# # Capture frames continuously
# try:
#     while True:
#         frame = grabScreen(region)  # Capture the specific region of the screen
        
#         if frame is not None:
#             frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
#             # Display the frame
#             cv2.imshow('Bonk Game Region', frame_bgr)
#             if cv2.waitKey(1) & 0xFF == ord('q'):  # Allow exiting the loop with 'q'
#                 break
# finally:
#     cv2.destroyAllWindows()  # Close all OpenCV windows



# main.py

import cv2
from screen_capture import grabScreen, getWindowHandle, bringWindowToFront
from new_object_detection import detect_players

# Get the window handle for the bonk.io window
window_name = 'bonk.io - Official Site: Play Bonk Here! - Google Chrome'
hwnd = getWindowHandle(window_name)
bringWindowToFront(hwnd)  # Bring the bonk.io window to the front

region = (245, 215, 880, 640)

# Capture frames continuously and process them
try:
    while True:
        frame = grabScreen(region=region)  # Capture the whole screen
        if frame is not None:
            processed_frame = detect_players(frame)  # Process the frame to detect players
            processed_frame = cv2.cvtColor(processed_frame, cv2.COLOR_RGB2BGR)
            cv2.imshow('Live Player Detection', processed_frame)  # Display the processed frame
            
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Allow exiting the loop with 'q'
                break
finally:
    cv2.destroyAllWindows()  # Close all OpenCV windows
