import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Preprocessed dataset/5206.jpg")
plt.imshow(img)

print("test")

detector = cv.SimpleBlobDetector_create()
keypoints = detector.detect(img)
print(len(keypoints))
print("test2")