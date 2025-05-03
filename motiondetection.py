import cv2
import numpy as np
import datetime
# Initialize the webcam
cap = cv2.VideoCapture('rtsp://admin:admin123@192.168.21.102:554/stream?mode=real&idc=1&ids=1')  # Use 0 for default webcam, or replace with video file path

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None  # Will be initialized when motion is detected

# Initialize variables
ret, frame1 = cap.read()
ret, frame2 = cap.read()
motion_detected = False

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Check for motion
    motion_detected = False
    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue
        motion_detected = True
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("CCTV Camera", frame1)

    # Start recording if motion is detected
    if motion_detected:
        if out is None:
            # Initialize video writer on first motion detection
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            out = cv2.VideoWriter(f'motion_{timestamp}.avi', fourcc, 20.0, (frame1.shape[1], frame1.shape[0]))
        out.write(frame1)

    # Update frames for motion detection
    frame1 = frame2
    ret, frame2 = cap.read()

    if not ret:
        break

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
if out:
    out.release()
cv2.destroyAllWindows()