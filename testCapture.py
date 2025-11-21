import cv2

cap = cv2.VideoCapture(0) # 0 = /dev/video0
ret, frame = cap.read()
cv2.imwrite("block.jpg", frame)
cap.release
