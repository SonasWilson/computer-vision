# removing noise from an image
import cv2

img = cv2.imread('cow-salt-peper.png') # a noisy image

# applying blurring
ksize=7
img_blur = cv2.blur(img, (ksize, ksize))
img_gaussian_blur = cv2.GaussianBlur(img, (ksize, ksize), 4)
img_median_blur = cv2.medianBlur(img, ksize)

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussian_blur', img_gaussian_blur)
cv2.imshow('img_median_blur', img_median_blur) #it worked great

cv2.waitKey(0)
