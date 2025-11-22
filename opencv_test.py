import time
import cv2
import numpy as np

def camOn():
    # Open the default camera (camera 0)
    cam = cv2.VideoCapture(1)

    # Get the default frame width and height
    #frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    #frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    #fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    #out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))
    
    while True:
        ret, imageFrame = cam.read()

        # Convert to HSV color space (better for color segmentation)
        hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
        
        # Define lower and upper bounds for the red hue.
        red_lower = np.array([136, 87, 111],  np.uint8)
        red_upper = np.array([180, 255, 255], np.uint8)
        red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

        # Morphological Transform, Dilation 
        # for each color and bitwise_and operator 
        # between imageFrame and mask determines 
        # to detect only that particular color 
        kernel = np.ones((5, 5), "uint8") 
        
        # For red color 
        red_mask = cv2.dilate(red_mask, kernel) 
        res_red = cv2.bitwise_and(imageFrame, imageFrame, mask = red_mask)

        # Creating contour to track red color 
        contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > 1000): 
                x, y, w, h = cv2.boundingRect(contour) 
                imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2) 
                
                cv2.putText(imageFrame, "Red Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))

        # Write the frame to the output file
        #out.write(frame)

        # Display the captured frame
        cv2.imshow('Does it RED???!?', imageFrame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the capture and writer objects
    cam.release()
    out.release()
    cv2.destroyAllWindows()

camOn()
