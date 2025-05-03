import face_recognition
from pathlib import Path
import cv2
import numpy as np
import csv
from datetime import datetime

# video_capture = cv2.VideoCapture("rtsp://admin@192.168.21.10:554/stream?mode=real&idc=1&ids=1")
video_capture = cv2.VideoCapture('rtsp://admin:admin123@192.168.21.102:554/stream?mode=real&idc=1&ids=1')

# triloki_images = face_recognition.__loader__("faces/triloki.jpeg")

triloki_images = face_recognition.Path.is_dir("faces/triloki.jpeg")
triloki_encoding = face_recognition.face_encodings(triloki_images)[0]

known_face_encoding = [triloki_encoding]
knonw_face_names = ["triloki"]

students = knonw_face_names.copy()

face_locations = []
face_encoding = []

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RG)

face_locations = face_recognition.face_locations(rgb_small_frame)
face_encoding = face_recognition.face_encoding(rgb_small_frame, face_locations)

for face_encoding in face_encoding:
    matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
    face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
    best_match_index = np.argmin(face_distance)

    if(matches[best_match_index]):
        name = knonw_face_names[best_match_index]

    if name in knonw_face_names:
        font = cv2.FONT_HERSHEY_COMPLEX
        buttomLeftCornerOfText = (10,100)        
        fontScale =1.5
        fontColor =(255, 0 ,0)
        thickness = 3
        LineType = 2
        cv2.putText(frame, name + "Present",buttomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

    if name in students:
        students.remove(name)
        current_date = now.strftime("%H-%M%S")
        lnwriter.writernow([name, current_date])


    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.distoryAllWindows()
f.close()


# import cv2

# #print("Before URL")
# cap = cv2.VideoCapture('rtsp://admin@192.168.21.220:554/ch0_0.264')
# #print("After URL")

# while True:

#     #print('About to start the Read command')
#     ret, frame = cap.read()
#     #print('About to show frame of Video.')
#     cv2.imshow("Capturing",frame)
#     #print('Running..')

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()