import cv2
import numpy as np

def mask_function(RGB):
    # Convert RGB image to HSV color space
    hsv_image = cv2.cvtColor(RGB, cv2.COLOR_BGR2HSV)

    # Define HSV threshold values
    lower_bound = np.array([0, 0, 166], dtype=np.uint8)  # [H_min, S_min, V_min]
    upper_bound = np.array([255, 168, 255], dtype=np.uint8)  # [H_max, S_max, V_max]

    # Create a mask based on the HSV thresholds
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    # Invert the mask
    mask = cv2.bitwise_not(mask)

    # Initialize the output masked image based on the input image
    masked_RGB_image = RGB.copy()

    # Set background pixels where the mask is False to zero
    masked_RGB_image[np.where(mask[:, :] == 0)] = 0

    return mask, masked_RGB_image
