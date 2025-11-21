import cv2

# reading webcam
webcam = cv2.VideoCapture(0)

# visualise
while True:
    ret, frame = webcam.read()

    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()