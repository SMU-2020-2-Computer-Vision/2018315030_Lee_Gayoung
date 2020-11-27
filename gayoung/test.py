import os
import cv2
import numpy as np
from matplotlib import pyplot as plt


# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a reference image
img_rgb = cv2.imread('test_background.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# Load a template image as grayscale
template = cv2.imread('fish.png', 0)
w, h = template.shape[::-1]  #template 이미지의 크기

# Apply template matching(image와 template가 겹치는 부분을 비교)
res = cv2.matchTemplate(img_gray, template , cv2.TM_CCOEFF_NORMED)
#최소 포인터, 최대 포인터, 최소 지점, 최대 지점
#min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)


# # Thresholding
threshold = 0.5
loc = np.where(res >= threshold)

# # Draw a bounding box (새로운점)
img_res = img_rgb.copy()
for pt in zip(*loc[::-1]):    # loc의 순서를 거꾸로 하여 튜플로 묶고 리스트로 만들어줌
    #cv2.rectangle(img_res, pt, (w, h), (0,0,255), 2)
    cv2.rectangle(img_res, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

# Display results
titles = ['Original', 'Template Matching']
images = [img_rgb, img_res]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))    
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
# cv2.imshow("template",img_rgb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
