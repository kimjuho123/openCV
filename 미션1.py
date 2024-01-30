# 가로 1000, 세로 1000 짜리 창을 만들고
import cv2
import numpy as np

src = np.zeros((1000, 1000, 3), dtype=np.uint8) 

# x : 250 , y:  250 에 길이가 250 인 정사각형을 그리시오
src = cv2.rectangle(src, (250, 250), (500, 500), (255, 0, 0), 5, cv2.LINE_8) 

# 본인의 영어 이름을 x : 700 , y:  100  위치에 나타내시오 
src = cv2.putText(src, "sumin", (700, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

cv2.imshow("src", src)
cv2.waitKey()
cv2.destroyAllWindows()