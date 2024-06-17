# # import cv2
# # import numpy as np
# # import json

# # import json

# # def get_ppm_from_file(file_path):
# #     try:
# #         with open(file_path, 'r') as file:
# #             map_data = json.load(file)
# #             return map_data.get("physics", {}).get("ppm", None)
# #     except FileNotFoundError:
# #         print(f"File not found: {file_path}")
# #         return None
# #     except json.JSONDecodeError:
# #         print(f"Error decoding JSON from file: {file_path}")
# #         return None


# # def mask_color(frame, color, color_range=np.array([10,10,10], np.uint8)):
# #     mask_lower = np.clip(color - color_range, 0, 255)
# #     mask_upper = np.clip(color + color_range, 0, 255)
# #     return cv2.inRange(frame, mask_lower, mask_upper)

# # def get_pos(frame, color=None):
# #     HSV_frame = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2HSV)
# #     color_range = np.array([10,10,10], np.uint8)
    
# #     if color is not None:
# #         ball_mask = mask_color(HSV_frame, color, color_range)
# #     else:
# #         blue_ball = np.array([93, 255, 212])
# #         blue_bg = np.array([96, 128, 96])
# #         gray_platform = np.array([0, 0, 45])
        
# #         blue_ball_mask = mask_color(HSV_frame, blue_ball, color_range)
# #         bg_mask = mask_color(HSV_frame, blue_bg, color_range)
# #         platform_mask = mask_color(HSV_frame, gray_platform, color_range)
        
# #         not_ball_mask = blue_ball_mask + bg_mask + platform_mask
# #         ball_mask = cv2.bitwise_not(not_ball_mask)
# #         ball_mask = cv2.erode(ball_mask, None, iterations=4)
    
# #     M = cv2.moments(ball_mask)
# #     is_ball, ball_x, ball_y = False, -1, -1
# #     if M["m00"] != 0:
# #         is_ball = True
# #         ball_x = round(M["m10"] / M["m00"], 2)
# #         ball_y = round(M["m01"] / M["m00"], 2)
    
# #     return is_ball, (ball_x, ball_y)

# # def calculate_player_size(ppm):
# #     map_scales = {
# #         1: 30,
# #         2: 25,
# #         3: 20,
# #         4: 17,
# #         5: 15,
# #         6: 13,
# #         7: 12,
# #         8: 10,
# #         9: 9,
# #         10: 8,
# #         11: 7,
# #         12: 6,
# #         13: 5
# #     }
# #     map_size = min(max((ppm - 2) // 23 + 1, 1), 13)  # Adjust the formula to fit the scale properly
# #     return map_scales.get(map_size, 10)  # Default to 10 if something goes wrong

# # def detect_players(img, ppm):
    
# #     player_size = calculate_player_size(ppm)
# #     imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #     threshold = cv2.adaptiveThreshold(imgGrey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# #     contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# #     detected_players = []

# #     for contour in contours:
# #         approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
# #         (x, y), radius = cv2.minEnclosingCircle(approx)
# #         center = (int(x), int(y))
# #         radius = int(radius)

# #         if radius > 0:
# #             contour_area = cv2.contourArea(contour)
# #             print('PPM: ', ppm)
# #             print("CONTOUR AREA: ", contour_area)
# #             circle_area = np.pi * (radius ** 2)
# #             x, y, w, h = cv2.boundingRect(contour)
# #             aspect_ratio = float(w) / h

# #             # Adjust player size detection based on the calculated player size
# #             if 0.6 <= contour_area / circle_area <= 1.2 and 0.7 <= aspect_ratio <= 1.3 and (0.8 * player_size) ** 2 * np.pi <= contour_area <= (1.2 * player_size) ** 2 * np.pi:
# #                 cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
# #                 cv2.putText(img, "Player", (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
# #                 detected_players.append((x, y, w, h))

# #     for (x, y, w, h) in detected_players:
# #         player_color = img[y:y+h, x:x+w].mean(axis=0).mean(axis=0)
# #         is_ball, ball_pos = get_pos(img, player_color)
        
# #         if is_ball:
# #             cv2.circle(img, (int(ball_pos[0]), int(ball_pos[1])), 10, (0, 255, 0), 2)
# #     print("PLAYER SIZE: ", player_size)
# #     return img

# import cv2
# import numpy as np
# import json

# def get_ppm_from_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             map_data = json.load(file)
#             return map_data.get("physics", {}).get("ppm", None)
#     except FileNotFoundError:
#         print(f"File not found: {file_path}")
#         return None
#     except json.JSONDecodeError:
#         print(f"Error decoding JSON from file: {file_path}")
#         return None

# def mask_color(frame, color, color_range=np.array([10,10,10], np.uint8)):
#     mask_lower = np.clip(color - color_range, 0, 255)
#     mask_upper = np.clip(color + color_range, 0, 255)
#     return cv2.inRange(frame, mask_lower, mask_upper)

# def get_pos(frame, color=None):
#     HSV_frame = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2HSV)
#     color_range = np.array([10,10,10], np.uint8)
    
#     if color is not None:
#         ball_mask = mask_color(HSV_frame, color, color_range)
#     else:
#         blue_ball = np.array([93, 255, 212])
#         blue_bg = np.array([96, 128, 96])
#         gray_platform = np.array([0, 0, 45])
        
#         blue_ball_mask = mask_color(HSV_frame, blue_ball, color_range)
#         bg_mask = mask_color(HSV_frame, blue_bg, color_range)
#         platform_mask = mask_color(HSV_frame, gray_platform, color_range)
        
#         not_ball_mask = blue_ball_mask + bg_mask + platform_mask
#         ball_mask = cv2.bitwise_not(not_ball_mask)
#         ball_mask = cv2.erode(ball_mask, None, iterations=4)
    
#     M = cv2.moments(ball_mask)
#     is_ball, ball_x, ball_y = False, -1, -1
#     if M["m00"] != 0:
#         is_ball = True
#         ball_x = round(M["m10"] / M["m00"], 2)
#         ball_y = round(M["m01"] / M["m00"], 2)
    
#     return is_ball, (ball_x, ball_y)

# def calculate_player_size(ppm):
#     map_scales = {
#         1: 30,
#         2: 25,
#         3: 20,
#         4: 17,
#         5: 15,
#         6: 13,
#         7: 12,
#         8: 10,
#         9: 9,
#         10: 8,
#         11: 7,
#         12: 6,
#         13: 5
#     }
#     map_size = min(max((ppm - 2) // 23 + 1, 1), 13)  # Adjust the formula to fit the scale properly
#     return map_scales.get(map_size, 10)  # Default to 10 if something goes wrong

# def detect_players(img, ppm):
    
#     player_size = calculate_player_size(ppm)
#     imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     threshold = cv2.adaptiveThreshold(imgGrey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#     contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#     detected_players = []

#     for contour in contours:
#         approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
#         (x, y), radius = cv2.minEnclosingCircle(approx)
#         center = (int(x), int(y))
#         radius = int(radius)

#         if radius > 0:
#             contour_area = cv2.contourArea(contour)
#             # print('PPM: ', ppm)
#             print("CONTOUR AREA: ", contour_area)
#             circle_area = np.pi * (radius ** 2)
#             x, y, w, h = cv2.boundingRect(contour)
#             aspect_ratio = float(w) / h

#             # Adjust player size detection based on the calculated player size
#             # if 0.6 <= contour_area / circle_area <= 1.2 and 0.7 <= aspect_ratio <= 1.3 and (0.8 * player_size) ** 2 * np.pi <= contour_area <= (1.2 * player_size) ** 2 * np.pi:
#             if 0.6 <= contour_area / circle_area <= 1.2 and 0.7 <= aspect_ratio <= 1.3 and 150 <= contour_area <= 2000:
#                 cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
#                 cv2.putText(img, "Player", (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#                 detected_players.append((x, y, w, h))

#     for (x, y, w, h) in detected_players:
#         player_color = img[y:y+h, x:x+w].mean(axis=0).mean(axis=0)
#         is_ball, ball_pos = get_pos(img, player_color)
        
#         if is_ball:
#             cv2.circle(img, (int(ball_pos[0]), int(ball_pos[1])), 10, (0, 255, 0), 2)
#     print("PLAYER SIZE: ", player_size)
#     return img


import cv2
import numpy as np
import json

def get_player_colors_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            player_data = json.load(file)
            player_colors = [player["avatar"]["bc"] for player in player_data if player]
            return player_colors
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {file_path}")
        return None

def get_map_color_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            map_data = json.load(file)
            return map_data.get("m", {}).get("dbid", None)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {file_path}")
        return None

def get_ppm_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            map_data = json.load(file)
            return map_data.get("physics", {}).get("ppm", None)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {file_path}")
        return None

def mask_color(frame, color, color_range=np.array([10,10,10], np.uint8)):
    mask_lower = np.clip(color - color_range, 0, 255)
    mask_upper = np.clip(color + color_range, 0, 255)
    return cv2.inRange(frame, mask_lower, mask_upper)

def get_pos(frame, color=None):
    HSV_frame = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2HSV)
    color_range = np.array([10,10,10], np.uint8)
    
    if color is not None:
        ball_mask = mask_color(HSV_frame, color, color_range)
    else:
        # blue_ball = np.array([93, 255, 212])
        ai_ball = np.array([0, 0, 0])
        blue_bg = np.array([51, 72, 92])
        gray_platform = np.array([0, 0, 45])
        
        ai_ball_mask = mask_color(HSV_frame, ai_ball, color_range)
        bg_mask = mask_color(HSV_frame, blue_bg, color_range)
        platform_mask = mask_color(HSV_frame, gray_platform, color_range)
        
        not_ai_mask = ai_ball_mask + bg_mask + platform_mask
        ball_mask = cv2.bitwise_not(not_ai_mask)
        ball_mask = cv2.erode(ball_mask, None, iterations=4)
    
    M = cv2.moments(ball_mask)
    is_ball, ball_x, ball_y = False, -1, -1
    if M["m00"] != 0:
        is_ball = True
        ball_x = round(M["m10"] / M["m00"], 2)
        ball_y = round(M["m01"] / M["m00"], 2)
    
    return is_ball, (ball_x, ball_y)

def calculate_contour_area_range(ppm, base_ppm=15, base_range=(150, 2000)):
    scale_factor = ppm / base_ppm
    return (int(base_range[0] * scale_factor), int(base_range[1] * scale_factor))

def detect_players(img, ppm):
    contour_area_range = calculate_contour_area_range(ppm)
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold = cv2.adaptiveThreshold(imgGrey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    detected_players = []

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        (x, y), radius = cv2.minEnclosingCircle(approx)
        center = (int(x), int(y))
        radius = int(radius)

        if radius > 0:
            contour_area = cv2.contourArea(contour)
            circle_area = np.pi * (radius ** 2)
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = float(w) / h

            # print(f"PPM : {ppm}, Contour Area: {contour_area}, Circle Area: {circle_area}, Aspect Ratio: {aspect_ratio}, Radius: {radius}, Contour Area Range: {contour_area_range}")

            if 0.6 <= contour_area / circle_area <= 1.2 and 0.7 <= aspect_ratio <= 1.3 and contour_area_range[0] <= contour_area <= contour_area_range[1]:
                cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
                cv2.putText(img, "Player", (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                detected_players.append((x, y, w, h))

    for (x, y, w, h) in detected_players:
        player_color = img[y:y+h, x:x+w].mean(axis=0).mean(axis=0)
        is_ball, ball_pos = get_pos(img, player_color)
        
        if is_ball:
            cv2.circle(img, (int(ball_pos[0]), int(ball_pos[1])), 10, (0, 255, 0), 2)

    return img
