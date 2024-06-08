# import cv2 
# import numpy as np

# img  = cv2.imread('BonkExample4.png')
# imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# threshold = cv2.adaptiveThreshold(imgGrey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


# for contour in contours:
#     approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)

#     # Fit a circle to the contour
#     (x, y), radius = cv2.minEnclosingCircle(approx)
#     center = (int(x), int(y))
#     radius = int(radius)

#     if radius > 0:
#         # Calculate the area of the contour and the area of the circle
#         contour_area = cv2.contourArea(contour)
#         circle_area = np.pi * (radius ** 2)

#         # Calculate the aspect ratio
#         x, y, w, h = cv2.boundingRect(contour)
#         aspect_ratio = float(w) / h

#         # Filter out contours that are not roughly circular
#         if 0.8 <= contour_area / circle_area <= 1.2 and 0.9 <= aspect_ratio <= 1.1 and 1000 < contour_area < 10000:
#             cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
#             cv2.putText(img, "Player", (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))




# cv2.imshow('Bonk Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2 
import numpy as np

img  = cv2.imread(r'C:\Users\user\OneDrive\Desktop\Projects\Bonkio\Bonk.io-AI-Bot\windows\BonkExample4.png')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold = cv2.adaptiveThreshold(imgGrey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)

    # Fit a circle to the contour
    (x, y), radius = cv2.minEnclosingCircle(approx)
    center = (int(x), int(y))
    radius = int(radius)

    if radius > 0:
        # Calculate the area of the contour and the area of the circle
        contour_area = cv2.contourArea(contour)
        circle_area = np.pi * (radius ** 2)

        # Calculate the aspect ratio
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = float(w) / h

        # Filter out contours that are not roughly circular
        if 0.6 <= contour_area / circle_area <= 1.2 and 0.7 <= aspect_ratio <= 1.3 and 500 < contour_area < 3000:
            cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
            cv2.putText(img, "Player", (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
img = cv2.resize(img, (800, 600))
cv2.imshow('Bonk Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
