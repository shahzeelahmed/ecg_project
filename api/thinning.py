import cv2
import numpy as np

def thinning(imbwaa):
    img = imbwaa.copy()
    
    # Perform thinning using morphological operation
    img = cv2.ximgproc.thinning(img, thinningType=cv2.ximgproc.THINNING_GUOHALL)

    # Invert the image
    k = ~img

    return k
