import cv2
import numpy as np
import digitization as digi
import thinning as thin

# Load the image
rgb1 = cv2.imread('api\ecg2 (1).jpg')

# Crop the image
cropped = cv2.selectROI(rgb1)
cropped = rgb1[int(cropped[1]):int(cropped[1] + cropped[3]), int(cropped[0]):int(cropped[0] + cropped[2])]

# Save the cropped image
cv2.imwrite('cropped.jpg', cropped)

# Convert to grayscale
gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

# Threshold the image
_, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Remove small objects
bw4 = cv2.morphologyEx(bw, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=1)

# Flip the image vertically
imbwaa = np.flip(bw4, axis=0)
[k] = thin(imbwaa)

# Run digitization script (you need to implement this part)
# You can import and use any Python functions or scripts you have for digitization.

# Display the cropped image
cv2.imshow('Cropped Image', cropped)



