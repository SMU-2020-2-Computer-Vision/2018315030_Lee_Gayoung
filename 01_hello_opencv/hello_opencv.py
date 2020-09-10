import cv2
import os

cwd = os.path.dirname(os.path.abspath(__file__))

os.chdir(cwd)

img = cv2.imread('butterfly.jpg')

cv2.imshow('image' ,img)

cv2.waitKey(0)
cv2.destroyAllWindows()


