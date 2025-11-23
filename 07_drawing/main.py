import cv2

img = cv2.imread('whiteboard.png')
print(img.shape)

# line
# start(x,y) end(x,y) color(bgr) thickness
img = cv2.line(img, (100,150), (500, 150), (0, 0, 255), 3)

# rectange
# topleft(x,y) bottomright(x,y) color thickness (-1 fill)
img = cv2.rectangle(img, (200, 220), (500, 440), (255,0,0), 5)
# img = cv2.rectangle(img, (200, 220), (500, 440), (255,0,0), -1)

# circle
# center, radius, color, thickness
img = cv2.circle(img, (700,400), 100, (0,255,0), 15)

# text
img = cv2.putText(img, "Hello", (300, 350), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 100, 100), 3)

cv2.imshow('img', img)
cv2.waitKey(0)