import cv2

# reading image
img = cv2.imread('image.jpg')

# writing image
img_out = cv2.imwrite('image_out.jpg', img)

# visualise the image
cv2.imshow('image', img)
cv2.waitKey(0)