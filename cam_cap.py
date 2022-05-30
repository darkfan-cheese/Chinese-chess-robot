import cv2

cap  = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    cv2.imshow('video', frame)
    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        cv2.imwrite('img8.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()
