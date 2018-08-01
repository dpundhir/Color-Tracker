import cv2
import numpy as np

def emptyFunction():
    pass

def main():
    
    img=np.zeros((512,512,3), 'uint8')
    winName="color selection"
    cv2.namedWindow(winName)
    
    cv2.createTrackbar('B', winName, 0 ,255, emptyFunction)    
    cv2.createTrackbar('G', winName, 0 ,255, emptyFunction)
    cv2.createTrackbar('R', winName, 0 ,255, emptyFunction)
    
    while(True):
        cv2.imshow(winName,img)
        
        if cv2.waitKey(1)==27:
            break
        
        blue=cv2.getTrackbarPos('B',winName)
        green=cv2.getTrackbarPos('G',winName)
        red=cv2.getTrackbarPos('R',winName)
        
        img[:] = [blue, green, red]
       ## print(blue,red,green)
        
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()