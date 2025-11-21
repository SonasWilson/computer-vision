import cv2

# reading video

vid = cv2.VideoCapture('video.mp4')
fps = vid.get(cv2.CAP_PROP_FPS) #for waitkey
delay = int(1000 / fps)

ret = True
while ret:
    ret, frame = vid.read()

    # if there are frames
    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(delay)

vid.release()
cv2.destroyAllWindows()