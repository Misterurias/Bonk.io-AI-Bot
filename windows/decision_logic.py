import cv2
import numpy as np

# Initialize previous positions
prev_player_x = None
prev_player_y = None

def process_screen(screen):
    # Convert the image to grayscale
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    # Use Canny edge detection to identify edges
    edges = cv2.Canny(gray, 50, 150)
    return edges

def find_obstacles(screen, edges):
    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    obstacles = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 10 and h > 10:  # Filter out small contours
            obstacles.append((x, y, w, h))
            cv2.rectangle(screen, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Draw rectangle around obstacles
    return obstacles, screen

def find_player_position(prev_gray, current_frame):
    global prev_player_x, prev_player_y

    # Convert the current frame to grayscale
    gray_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    # Ensure both frames are of the same size
    if prev_gray.shape != gray_frame.shape:
        raise ValueError("The initial and current frames do not have the same dimensions")

    # Apply frame differencing
    frame_diff = cv2.absdiff(prev_gray, gray_frame)
    # cv2.imshow("Frame Difference", frame_diff)  # Display the frame difference for debugging

    # Apply Canny edge detection
    edges = cv2.Canny(frame_diff, 50, 150)
    # cv2.imshow("Edges", edges)  # Display the edges for debugging

    # Apply morphological operations to clean up the edges
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    edges = cv2.dilate(edges, kernel, iterations=2)
    edges = cv2.erode(edges, kernel, iterations=2)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    player_pos = None
    for contour in contours:
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / h

        print(f"Contour area: {area}, Aspect ratio: {aspect_ratio}, Bounding box: ({x}, {y}, {w}, {h})")

        # Adjust these thresholds if needed
        if area > 100 and 0.5 < aspect_ratio < 2:  # Heuristic to classify as player
            cx, cy = x + w // 2, y + h // 2
            player_pos = (x, y, w, h)
            prev_player_x, prev_player_y = cx, cy
            print(f"Detected Player Position: ({cx}, {cy})")
            break

    if player_pos is None:
        print("No player detected.")

    return player_pos, (prev_player_x, prev_player_y)

def find_goal(screen):
    # Convert to HSV to find a specific color (assuming goal has a unique color)
    hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
    # Define the color range for detecting the goal (adjust the values accordingly)
    lower_color = np.array([79, 41, 58])
    upper_color = np.array([133, 133, 149])
    mask = cv2.inRange(hsv, lower_color, upper_color)
    # Find contours in the masked image
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        return (x, y, w, h)  # Return the bounding box
    return None

def make_decision(obstacles, goal, player_pos):
    if goal is None or player_pos is None:
        return 'none'
    
    goal_x, goal_y, _, _ = goal  # Extract the coordinates from the bounding box
    player_x, player_y, _, _ = player_pos  # Extract the coordinates from the bounding box
    
    if goal_x > player_x and goal_y < player_y:
        return 'up-right'
    elif goal_x < player_x and goal_y < player_y:
        return 'up-left'
    elif goal_x > player_x and goal_y > player_y:
        return 'down-right'
    elif goal_x < player_x and goal_y > player_y:
        return 'down-left'
    elif goal_x > player_x:
        return 'right'
    elif goal_x < player_x:
        return 'left'
    elif goal_y > player_y:
        return 'down'
    else:
        return 'up'
    
def draw_player_position(screen, player_position):
    if player_position is not None:
        x, y, w, h = player_position
        cv2.rectangle(screen, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle around player
    return screen
