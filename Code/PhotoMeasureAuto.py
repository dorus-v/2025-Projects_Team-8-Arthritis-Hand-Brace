import cv2
import os
from pathlib import Path

photo_table = []
area_table = []

for i in os.listdir(r"C:\Users\qyoti\Documents\GitHub\Arthritis-Hand-Brace-Project-Natuur--en-Sterrenkunde"):
    if i.endswith(".jpg") or i.endswith(".JPG"):
        photo_table.append(os.path.abspath(i))

print(photo_table)

counter = 0
for photo in photo_table:
    counter = counter + 1
    savename = "Image" + str(counter) + ".jpeg"

    img = cv2.imread(photo)

    img_selection = img[1900:2000, 1500:4500]

    img_gray = cv2.cvtColor(img_selection, cv2.COLOR_BGR2GRAY)

    ret, thresh  = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img_selection, contours, -1, (0,255,0), 3)

    cv2.rectangle(img, (1500, 1900), (4500, 2000), (0, 0, 255), 2)
    area = cv2.contourArea(contours[0])
    area_table.append(area)
    cv2.imwrite(savename, img)

ratio = area_table[1] / area_table[0]

ratio = min(ratio, 1/ratio)

print("Image 1 area:", area_table[0])
print("Image 2 area:", area_table[1])
print("Ratio:", ratio)