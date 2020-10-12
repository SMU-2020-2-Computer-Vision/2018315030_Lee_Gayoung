import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Load a grayscale image
img = cv2.imread('noisy2.png', 0)

# Blur the image
blur = cv2.GaussianBlur(img, (5,5), 0)

# Find normalized_histogram, and its cumulative distribution function
hist = cv2.calcHist([blur], [0], None, [256], [0,256])
hist_norm = hist.ravel()/hist.max()
Q = hist_norm.cumsum()

# Find probabilities
bins = np.arange(256)

fn_min = np.inf
thresh = -1

for i in range(1,256):
    p1,p2 = np.hsplit(hist_norm,[i])    # probabilities
    q1,q2 = Q[i], Q[255]-Q[i]           # cum sum of classes
    b1,b2 = np.hsplit(bins,[i])         # weights

    # Finding means and variances
    m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
    v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2

    # calculates the minimization function
    fn = v1*q1 + v2*q2
    if fn < fn_min:
        fn_min = fn
        thresh = i

# Compare with the OpenCV function
ret, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(thresh,ret)