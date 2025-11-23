import cv2

img = cv2.imread('handwritten.png')

# 1. applying simple threshold
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

# 2. applying adaptive threshold (gaussian & mean)
adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21,30)
# adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21,30)

cv2.imshow('img', img)
cv2.imshow('simple_thresh', thresh)
cv2.imshow('adaptive_thresh', adaptive_thresh)

cv2.waitKey(0)