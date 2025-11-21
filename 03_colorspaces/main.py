import cv2

img = cv2.imread('bird.jpeg')
# This is BGR

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imwrite('img_rgb.jpeg', img_rgb)
cv2.imwrite('img_gray.jpeg', img_gray)
cv2.imwrite('img_hsv.jpeg', img_hsv)

cv2.imshow('image', img)
cv2.imshow('img_rgb', img_rgb)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_hsv', img_hsv)
cv2.waitKey(0)