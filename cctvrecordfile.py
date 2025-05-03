#import numpy as np
import cv2
import time
from datetime import datetime
import os

# open a video stream
cap = cv2.VideoCapture('rtsp://admin:admin123@192.168.21.102:554/stream?mode=real&idc=1&ids=1') # Do you want to test with the local camera?

w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS) 
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

while True:
    dt  = datetime.now().isoformat().replace(':','-').replace('.','-')
    out = cv2.VideoWriter('log/output' + dt + '.mp4', fourcc, fps, (int(w),int(h)))

    # start timer
    start_time = time.time()

    # Capture video from camera per 60 seconds
    while (int(time.time() - start_time) < 60):
        ret, frame = cap.read()
        if ret==True:

            #frame = cv2.flip(frame,0) # Do you want to FLIP the images?

            out.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    out.release()

    list_of_files = os.listdir('log')
    full_path = ["log/{0}".format(x) for x in list_of_files]

    if len(list_of_files) == 15:
        oldest_file = min(full_path, key=os.path.getctime)
        os.remove(oldest_file)

cap.release()

cv2.destroyAllWindows()
