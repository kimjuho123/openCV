# 여러분들의 왼쪽눈을 감지하여 사각형을 그려 보시오
# python -m pip install opencv-python
import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1000) # 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 800) # 높이

# 왼쪽눈 인식 모델 가져오기
eye_cascade = cv2.CascadeClassifier("data\haarcascades\haarcascade_lefteye_2splits.xml")

while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read()
    eyes = eye_cascade.detectMultiScale(frame, 1.03 , 5)
    
    for x,y,w,h in eyes:
        print(x,y,w,h)
        src = cv2.rectangle(src, (x,y), (x+w , y+h), (255, 0, 0), 5, cv2.LINE_8) 
    cv2.imshow("VideoFrame", frame) # imshow : 보여주기 


capture.release()
cv2.destroyAllWindows()