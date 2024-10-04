import cv2

webcam = cv2.VideoCapture(0)

while True:
    cam, frame = webcam.read()
    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()