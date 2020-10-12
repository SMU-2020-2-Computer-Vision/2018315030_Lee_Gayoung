import cv2
import os

cwd = os.path.dirname(os.path.abspath(__file__))

os.chdir(cwd)

img = cv2.imread('butterfly.jpg')

print(type(img))
print(img.ndim)  
print(img.shape)
print(img.size)
print(img.dtype)


cv2.imshow('image' ,img)

cv2.waitKey(0)
cv2.destroyAllWindows()


