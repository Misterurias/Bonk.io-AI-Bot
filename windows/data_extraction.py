# import pandas as pd
# import cv2
# import os
# import json
# import numpy as np

# data = {
#     'frame': [],
#     'object_id': [],
#     'object_type': [],
#     'object_x': [],
#     'object_y': [],
#     # Add more fields as needed
# }

# # Load the path from the configuration file
# with open('config.json', 'r') as config_file:
#     config = json.load(config_file)
# video_frames_dir = config['video_frames_dir']

# # Get the list of frame files
# frame_files = sorted([f for f in os.listdir(video_frames_dir) if os.path.isfile(os.path.join(video_frames_dir, f))])

# # Define parameters for motion detection
# min_contour_area = 500  # Minimum contour area to be considered as motion
# frame_diff_threshold = 25  # Threshold to consider a difference as motion

# # Load the first frame
# prev_frame_path = os.path.join(video_frames_dir, frame_files[0])
# prev_frame = cv2.imread(prev_frame_path, cv2.IMREAD_GRAYSCALE)

# for i, frame_file in enumerate(frame_files[1:], start=1):
#     frame_path = os.path.join(video_frames_dir, frame_file)
#     frame = cv2.imread(frame_path)
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Compute the absolute difference between the current frame and the previous frame
#     frame_diff = cv2.absdiff(gray_frame, prev_frame)
    
#     # Threshold the difference image to get the foreground mask
#     _, motion_mask = cv2.threshold(frame_diff, frame_diff_threshold, 255, cv2.THRESH_BINARY)

#     # Find contours in the motion mask
#     contours, _ = cv2.findContours(motion_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Draw the contours on the original frame
#     for contour in contours:
#         if cv2.contourArea(contour) >= min_contour_area:
#             x, y, w, h = cv2.boundingRect(contour)
#             # Log the detected positions
#             data['frame'].append(i)
#             data['object_id'].append(len(data['frame']))  # Unique object ID, can be improved with actual tracking
#             data['object_type'].append('unknown')  # You can add logic to differentiate types if possible
#             data['object_x'].append(x + w // 2)
#             data['object_y'].append(y + h // 2)
#             # Add more fields as needed

#     # Update the previous frame
#     prev_frame = gray_frame

# # Save the data to a CSV file
# df = pd.DataFrame(data)
# df.to_csv('game_data.csv', index=False)


import pandas as pd
import cv2
import os
import json
import numpy as np

data = {
    'frame': [],
    'object_id': [],
    'object_type': [],
    'object_x': [],
    'object_y': [],
    'player_direction': [],
    'arrow_direction': []
}

# Load the path from the configuration file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
video_frames_dir = config['video_frames_dir']

# Get the list of frame files
frame_files = sorted([f for f in os.listdir(video_frames_dir) if os.path.isfile(os.path.join(video_frames_dir, f))])

# Define parameters for motion detection
min_contour_area = 100  # Minimum contour area to be considered as motion
frame_diff_threshold = 25  # Threshold to consider a difference as motion

# Load the first frame
prev_frame_path = os.path.join(video_frames_dir, frame_files[0])
prev_frame = cv2.imread(prev_frame_path, cv2.IMREAD_GRAYSCALE)

# Initialize previous positions
prev_player_x = None
prev_player_y = None
prev_arrow_positions = {}

def determine_direction(prev_x, prev_y, curr_x, curr_y):
    if prev_x is None or prev_y is None:
        return 'NONE'
    delta_x = curr_x - prev_x
    delta_y = curr_y - prev_y
    if abs(delta_x) > abs(delta_y):
        if delta_x > 0 and delta_y > 0:
            return 'DOWN-RIGHT'
        elif delta_x > 0 and delta_y < 0:
            return 'UP-RIGHT'
        elif delta_x < 0 and delta_y > 0:
            return 'DOWN-LEFT'
        elif delta_x < 0 and delta_y < 0:
            return 'UP-LEFT'
        elif delta_x > 0:
            return 'RIGHT'
        else:
            return 'LEFT'
    else:
        if delta_y > 0:
            return 'DOWN'
        else:
            return 'UP'

for i, frame_file in enumerate(frame_files[1:], start=1):
    frame_path = os.path.join(video_frames_dir, frame_file)
    frame = cv2.imread(frame_path)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Compute the absolute difference between the current frame and the previous frame
    frame_diff = cv2.absdiff(gray_frame, prev_frame)
    
    # Threshold the difference image to get the foreground mask
    _, motion_mask = cv2.threshold(frame_diff, frame_diff_threshold, 255, cv2.THRESH_BINARY)

    # Find contours in the motion mask
    contours, _ = cv2.findContours(motion_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the original frame
    for contour in contours:
        if cv2.contourArea(contour) >= min_contour_area:
            x, y, w, h = cv2.boundingRect(contour)
            cx, cy = x + w // 2, y + h // 2

            # Heuristic to classify as player or arrow
            if w > 30 and h > 30:  # Assuming players are larger than arrows
                object_type = 'player'
                player_direction = determine_direction(prev_player_x, prev_player_y, cx, cy)
                arrow_direction = 'NONE'
                prev_player_x, prev_player_y = cx, cy
            else:
                object_type = 'arrow'
                player_direction = 'NONE'
                arrow_direction = determine_direction(prev_arrow_positions.get(i, [None, None])[0], prev_arrow_positions.get(i, [None, None])[1], cx, cy)
                prev_arrow_positions[i] = [cx, cy]

            # Log the detected positions and directions
            data['frame'].append(i)
            data['object_id'].append(len(data['frame']))  # Unique object ID, can be improved with actual tracking
            data['object_type'].append(object_type)
            data['object_x'].append(cx)
            data['object_y'].append(cy)
            data['player_direction'].append(player_direction)
            data['arrow_direction'].append(arrow_direction)

    # Update the previous frame
    prev_frame = gray_frame

# Save the data to a CSV file
df = pd.DataFrame(data)
df.to_csv('game_data.csv', index=False)
