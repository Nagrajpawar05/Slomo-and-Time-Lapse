import cv2
cap=cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'XVID')  #(*'XVID') = ('X','V','I','D') =>codec format for .avi file
output=cv2.VideoWriter('output_video.avi',fourcc,100.0,(640,480)) #20.0 => 20 frames per second FPS(normal FPS in python)( for time_lapse 100.0FPS..you can even increases if requied)
                                                                 #(640,480) =>default width and height of each frame

#cap.set(3,1208) #set the width to 1208 if required
#cap.set(4,920) #set height

while(cap.isOpened()):#cap.isOPened()=>returns true if camera is opened
    ret,frame=cap.read()
    if ret==True :
        output.write(frame)
        cv2.imshow('output',frame)
        if cv2.waitKey(1)==ord('q'):   # waitakey(0) => for single frame
                                                 # waitKey(1) => for multipe frames(videos)
            break
    else:
        break

cap.release()
output.release()
