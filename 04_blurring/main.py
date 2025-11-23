import cv2

img = cv2.imread('image.png')

# blurring for noise removal
k_size = 5
img_blur = cv2.blur(img, (k_size, k_size))
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 3)
img_median_blur = cv2.medianBlur(img, k_size)

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussian_blur', img_gaussian_blur)
cv2.imshow('img_median_blur', img_median_blur)

cv2.waitKey(0)