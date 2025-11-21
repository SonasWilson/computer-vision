import cv2

img = cv2.imread("dog.jpg")
print(f"Size of image: {img.shape}") #height, width, channel nos

# resizing - half
resized_img = cv2.resize(img, (500, 500)) #width, height
print(f"Size of image: {resized_img.shape}")

cv2.imshow('image', img)
cv2.imshow('resized image', resized_img)
cv2.waitKey(0)