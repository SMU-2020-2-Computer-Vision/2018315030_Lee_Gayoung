import numpy as np
import cv2
import random

# Global variables
mouse_is_pressed = False
mouse_start_x = -1
mouse_start_y = -1
mode=  True
color = (255, 255, 255)
angle = 0
stratAngle = 0
endAngle = 360

# Mouse event callback
def mouse_callback(event, x, y, flags, param):
    global mouse_is_pressed, mouse_start_x, mouse_start_y, color

    # Left button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        # Flag on
        mouse_is_pressed = True

        # Record the mouse position
        mouse_start_x = x
        mouse_start_y = y

        # Pick a random color
        color = (random.randrange(256), random.randrange(256), 
                 random.randrange(256))

        
    
    # Left button released
    elif event == cv2.EVENT_LBUTTONUP:
        # Flag off
        mouse_is_pressed = False

        if mode == True:
            
            # Draw a rectangle
            cv2.rectangle(img_color, (mouse_start_x, mouse_start_y), (x, y), color, -1)

        elif:
           cv2.ellipse(img_color,(mouse_start_x ,  mouse_start_y), (x-mouse_start_x ,  y-mouse_start_y), angle,stratAngle,endAngle, color, -1)

        elif:
             cv2.circle(img_color, (x, y), 5 ,color, -1)

        
    
    elif event == cv2.EVENT_MOUSEMOVE:
    # Flag on
        mouse_is_pressed == True

            if mode ==True:
                cv2.rectangle(img_color, (mouse_start_x, mouse_start_y), (x, y), color, -1)

            elif:
                cv2.ellipse(img_color,(mouse_start_x ,  mouse_start_y), (x-mouse_start_x ,  y-mouse_start_y), angle,stratAngle,endAngle, color, -1)

            elif:
                cv2.circle(img_color, (x, y), 5 ,color, -1)


# Create a black image
rows = 480
cols = 640
img_color = np.zeros((rows, cols, 3), np.uint8)

# Create a window
winname = 'Mouse Events'
cv2.namedWindow(winname)

# Register the mouse callback function
cv2.setMouseCallback(winname, mouse_callback)

# Infinite loop
while True:
    cv2.imshow(winname, img_color)
    key = cv2.waitKey(1)
   
    if key == ord('m'):
       mode = not mode
    elif key == 27: break
          
cv2.destroyAllWindows()