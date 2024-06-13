# import cv2 
# import numpy as np


# def getContours(screen):
#     img  = cv2.imread(screen)
#     imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     threshold = cv2.adaptiveThreshold(imgGrey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#     contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#     for contour in contours:
#         approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)

#         # Fit a circle to the contour
#         (x, y), radius = cv2.minEnclosingCircle(approx)
#         center = (int(x), int(y))
#         radius = int(radius)

#         if radius > 0:
#             # Calculate the area of the contour and the area of the circle
#             contour_area = cv2.contourArea(contour)
#             circle_area = np.pi * (radius ** 2)

#             # Calculate the aspect ratio
#             x, y, w, h = cv2.boundingRect(contour)
#             aspect_ratio = float(w) / h

#             # Filter out contours that are not roughly circular
#             if 0.6 <= contour_area / circle_area <= 1.2 and 0.7 <= aspect_ratio <= 1.3 and 1200 < contour_area < 3000:
#                 cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
#                 cv2.putText(img, "Player", (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#     img = cv2.resize(img, (800, 600))
#     return img



# new_object_detection.py

import cv2
import numpy as np

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
        blue_ball = np.array([93, 255, 212])
        blue_bg = np.array([96, 128, 96])
        gray_platform = np.array([0, 0, 45])
        
        blue_ball_mask = mask_color(HSV_frame, blue_ball, color_range)
        bg_mask = mask_color(HSV_frame, blue_bg, color_range)
        platform_mask = mask_color(HSV_frame, gray_platform, color_range)
        
        not_ball_mask = blue_ball_mask + bg_mask + platform_mask
        ball_mask = cv2.bitwise_not(not_ball_mask)
        ball_mask = cv2.erode(ball_mask, None, iterations=4)
    
    M = cv2.moments(ball_mask)
    is_ball, ball_x, ball_y = False, -1, -1
    if M["m00"] != 0:
        is_ball = True
        ball_x = round(M["m10"] / M["m00"], 2)
        ball_y = round(M["m01"] / M["m00"], 2)
    
    return is_ball, (ball_x, ball_y)

def detect_players(img):
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

            #NEED TO IMPLEMENT PLAYER SIZE FOR DIFFERENT MAPS --> 13 Different sizes --> Need to find a way to calculate map size for correct player contour area
            #ALSO NEED TO IGNORE DEATH ARROW BOW
            if 1 <= contour_area / circle_area <= 1.2 and 0.7 <= aspect_ratio <= 1.3 and 100 < contour_area < 200:
                cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
                cv2.putText(img, "Player", (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                detected_players.append((x, y, w, h))

    for (x, y, w, h) in detected_players:
        player_color = img[y:y+h, x:x+w].mean(axis=0).mean(axis=0)
        is_ball, ball_pos = get_pos(img, player_color)
        
        if is_ball:
            cv2.circle(img, (int(ball_pos[0]), int(ball_pos[1])), 10, (0, 255, 0), 2)

    return img
