import cv2
import os

cwd = os.path.dirname(os.path.abspath(__file__))

os.chdir(cwd)

img = cv2.imread('butterfly.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('butterfly_gray.jpg',img_gray)


cv2.imshow('color_image' , img)
cv2.imshow('gray_image' , img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


