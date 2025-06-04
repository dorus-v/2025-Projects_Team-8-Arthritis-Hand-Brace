import cv2

img_before = cv2.imread(r"C:\Users\qyoti\Documents\GitHub\Arthritis-Hand-Brace-Project-Natuur--en-Sterrenkunde\Media\Foto\IMG_1926_crop_cutout.jpg")
img_before_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)

thresh  = cv2.adaptiveThreshold(img_before_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 10)


contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_before, contours, -1, (0,255,0), 3)
area = cv2.contourArea(contours[0])

cv2.imwrite('Object.jpeg', img_before)
cv2.waitKey(0)

cv2.imwrite('object_with_contours.jpg', img_before)