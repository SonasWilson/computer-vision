# global threshold

import cv2

img = cv2.imread('bear.jpg')

# applying threshold value
# below 80 means 0 and above means 255
# convert image to gray
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
cv2.imwrite('sthresh_without_blur.jpg', thresh)

# to remove the noise apply blur
img_gray = cv2.blur(img_gray, (10,10))
ret, thresh_blur = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
cv2.imwrite('sthresh_with_blur.jpg', thresh_blur)

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.imshow('thresh_blur', thresh_blur)
cv2.waitKey(0)
