import cv2

img = cv2.imread(r"C:\Users\qyoti\Documents\GitHub\Arthritis-Hand-Brace-Project-Natuur--en-Sterrenkunde\Media\Foto\IMG_1926_crop_cutout.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh  = cv2.threshold(img_gray, 240, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,0), 3)
area = cv2.contourArea(contours[0])

print("area:" , area)

cv2.imwrite('Object.jpeg', img)