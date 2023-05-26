import numpy as np

import cv2

cap = cv2.VideoCapture(0)


tr, frame = cap.read()
print(frame)
cv2.imwrite('img.jpg', frame)

key = cv2.waitKey(0)

cv2.destroyAllWindows()
cap.release()



