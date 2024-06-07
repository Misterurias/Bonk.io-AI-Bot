import pandas as pd
import cv2
import os
import json

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

# Initialize object ID counter
object_id_counter = 0

# Load the first frame
prev_frame_path = os.path.join(video_frames_dir, frame_files[0])
prev_frame = cv2.imread(prev_frame_path)
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

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

for frame_index, frame_file in enumerate(frame_files[1:], start=1):
    frame_path = os.path.join(video_frames_dir, frame_file)
    frame = cv2.imread(frame_path)

    if frame is None:
        continue

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply frame differencing
    frame_diff = cv2.absdiff(prev_gray, gray_frame)

    # Apply Canny edge detection
    edges = cv2.Canny(frame_diff, 50, 150)

    # Apply morphological operations to clean up the edges
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    edges = cv2.dilate(edges, kernel, iterations=2)
    edges = cv2.erode(edges, kernel, iterations=2)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the original frame and extract data
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 50:  # Filter out small contours
            x, y, w, h = cv2.boundingRect(contour)
            cx, cy = x + w // 2, y + h // 2

            # Heuristic to classify as player or arrow
            if area > 500:
                object_type = 'player'
                color = (0, 255, 0)  # Green for players
                direction = determine_direction(prev_player_x, prev_player_y, cx, cy)
                prev_player_x, prev_player_y = cx, cy
                player_direction = direction
                arrow_direction = 'NONE'
            else:
                object_type = 'arrow'
                color = (0, 0, 255)  # Red for arrows
                direction = determine_direction(prev_arrow_positions.get(object_id_counter, [None, None])[0], prev_arrow_positions.get(object_id_counter, [None, None])[1], cx, cy)
                prev_arrow_positions[object_id_counter] = [cx, cy]
                player_direction = 'NONE'
                arrow_direction = direction

            # Log the detected positions and direction
            data['frame'].append(frame_index)
            data['object_id'].append(object_id_counter)
            data['object_type'].append(object_type)
            data['object_x'].append(cx)
            data['object_y'].append(cy)
            data['player_direction'].append(player_direction)
            data['arrow_direction'].append(arrow_direction)
            object_id_counter += 1

            # Draw a rectangle around the detected object
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

            # # Print direction if it's a player or arrow
            # if object_type == 'player':
            #     print(f"Frame: {frame_index}, Player Direction: {player_direction}")
            # elif object_type == 'arrow':
            #     print(f"Frame: {frame_index}, Arrow Direction: {arrow_direction}")

    # Display the frame with outlined objects
    cv2.imshow('Detected Players and Arrows', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Update the previous frame
    prev_gray = gray_frame

cv2.destroyAllWindows()

# Save the data to a CSV file
df = pd.DataFrame(data)
df.to_csv('game_data.csv', index=False)


