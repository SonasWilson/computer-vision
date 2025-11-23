import cv2

img = cv2.imread('bird.jpeg')

img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

cv2.imshow('img', img)
cv2.imshow('img_bgr', img_bgr)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_hsv', img_hsv)

cv2.waitKey(0)