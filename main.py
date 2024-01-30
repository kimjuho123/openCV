# python -m pip install opencv-python
import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
v = 0
while cv2.waitKey(33) != ord("q"):  # ord("a") == 97 
    ret, frame = capture.read()     # ret : T/F , frame : 영상정보
    # x :100 , y : 100 인 위치에 너비 300 높이 250 인 사각형을 그려 보시오 
    frame = cv2.rectangle(frame, (100+v,100+v), (400+v, 350+v), (255, 0, 0), 5, cv2.LINE_8)
    v += 1
    if v  > 300 : v = 0
    cv2.imshow("VideoFrame", frame)


capture.release()
cv2.destroyAllWindows()