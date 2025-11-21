import cv2

img = cv2.imread("dog.jpg")
print(f"Original image size:", img.shape)

# cropping
cropped_img = img[150:950, 270:780]
print(f"Cropped image size:", cropped_img)

# visualize
cv2.imshow("image", img)
cv2.imshow("cropped image", cropped_img)
cv2.waitKey(0)

