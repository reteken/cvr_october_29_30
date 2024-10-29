import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    print(frame.shape)
    height, width, _ = frame.shape
    lenth = 50
    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    frame[height // 2 - lenth:height // 2 + lenth + 1, width // 2 - lenth:width // 2 + lenth + 1, 2] = 0
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1)
    if key == ord(' '):
        break
    # print(ret)
    # print(frame)
    # break

cv2.destroyAllWindows()
cap.release()

