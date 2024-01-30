# python -m pip install opencv-python
import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1000) # 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 800) # 높이

# 얼굴인식 모델 가져오기 
smile_cascade = cv2.CascadeClassifier(".\opencv\openCV_sumin\data\haarcascades\haarcascade_smile.xml")

while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    smiles = smile_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.5,
        minNeibors=15,
        minSize =(25,25)
    )
    if len(smiles) > 0:
        for x,y,w,h in smiles:
            frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 5, cv2.LINE_8) 
    print(smiles)
    cv2.imshow("VideoFrame", frame) # imshow : 보여주기 


capture.release()
cv2.destroyAllWindows()