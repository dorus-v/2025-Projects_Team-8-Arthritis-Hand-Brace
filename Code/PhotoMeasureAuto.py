import cv2
import os
from pathlib import Path

photo_table = []
area_table = []

for i in os.listdir(r"C:\Users\qyoti\Documents\GitHub\Arthritis-Hand-Brace-Project-Natuur--en-Sterrenkunde"):
    if i.endswith(".jpg") or i.endswith(".JPG"):
        photo_table.append(os.path.abspath(i))

print(photo_table)

for photo in photo_table:
    img = cv2.imread(photo)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh  = cv2.threshold(img_gray, 240, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0,255,0), 3)
    area = cv2.contourArea(contours[0])
    area_table.append(area)

ratio = area_table[1] / area_table[0]

print(ratio)