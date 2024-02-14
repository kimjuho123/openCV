        
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(model_complexity=0,min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) 

        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                x1,x2,y1,y2 = 0,0,0,0
                for id  , lm in enumerate(hand.landmark):
                    h,w,c = image.shape
                    
                    cx ,cy = int(lm.x*w) , int(lm.y*h)
                    print(id , " : " , (cx , cy) , 20 ,(255,0,0) , cv2.FILLED)
                    if id == 8:
                        cv2.circle(image , (cx , cy) , 20 ,(255,0,0) , cv2.FILLED)
                        x1 , y1 = cx , cy
                    if id == 12:
                        cv2.circle(image , (cx , cy) , 20 ,(255,0,0) , cv2.FILLED)
                        x2 , y2 = cx , cy    
                cv2.rectangle(image , (x1 ,y1) , (x2 , y2) , (255,0,0) , cv2.FILLED)

        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
