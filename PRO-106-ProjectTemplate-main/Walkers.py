import cv2
frames = []

# Create our body classifier

body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    
    bodies = body_cascade.detectMultiScale(grey,1.1,1)

    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in bodies:
       # syntax cv2.retangle(which image,(starting x,y position),(ending x,y position),(color in BGR format),(thickenss
       # of the line of square made
       # ))
       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)

    frames.append(frame)

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

count = len(frames)
current = cv2.imread(frames[0])

height,width,channels = current.shape

size = (width,height)

out = cv2.VideoWriter("project1.mp4",cv2.VideoWriter_fourcc(*"DIVX"),5,size)

for i in range(count-1,0,-1):
    current = cv2.imread(frames[i])
    out.write(current)

out.release()
cap.release()
cv2.destroyAllWindows()
