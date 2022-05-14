
import cv2 
import mediapipe as mp 
import time #used to check the frame rate
import pyautogui

cap = cv2.VideoCapture(0) #create the video object
mpHands = mp.solutions.hands #intilialize the class of hands
hands = mpHands.Hands() #declare the Hands functions in the class above
mpDraw =mp.solutions.drawing_utils #allows the mapping of point to be shown on your hands 
screenWidth, screenHeight = pyautogui.size()

pTime = 0
cTime = 0
#imgX = 3000
#imgY = 3000

lms = []
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image',screenWidth, screenHeight)
while True: #while true means loop forever
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert the image procing from BRG(OpenCV default) to RGB(mediapipe default)
    results = hands.process(imgRGB) #process function from the MediaPipe library to store the hands image that have been converted
     #print(results.multi_hand_landmarks) # allows to reults to shows if there is hand showing in the image
    if results.multi_hand_landmarks:  
        for handLms in results.multi_hand_landmarks:# for each hand in the results that detect hand
            idArray = [] 
            for id, lm in enumerate(handLms.landmark): #handlms.lanmark function contains the information about the landmarks
                #print(id,lm) # for every frame per second the it print the id number and landmark position 
                h,w, c = img.shape # finding the width , height, channel of the image
                cx, cy = int(lm.x*w), int(lm.y*h)
                Mx, My = int(lm.x*screenWidth), int(lm.y*screenHeight)
                idArray.append(lm.y)
                lmlist = []
                #print(id, cx, cy) # the id is specify the specific landmark and it orientation
                if id == 9:
                    pyautogui.moveTo(Mx, My) #moves mouse with landmark 9
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            
            if idArray[8]>idArray[6]:
                print(idArray[8])
                pyautogui.click()    


                
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) #Not RGB image becuase we not displaying imgRGB rather that is for mp processing
            #handlms is repersenting a single hand 
    cTime = time.time() # current time
    fps = 1/(cTime-pTime) # frame per second 
    pTime = cTime
    cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_COMPLEX,
               3, (255, 0, 255), 3) #shows the frame per second on the img
    cv2.imshow("Image", img)
    cv2.waitKey(1) #returns an int. Allows to display window for 1 millisecond
    # while loop is infinite so therefore it is a sequence of images percieved as a continous video
    #The function does not wait exactly 1 ms, it will wait atleast 1 ms. Depending on what is runnning on you computer at the time.
   
 