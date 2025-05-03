# from flask import Flask, render_template, Response
# import cv2

# app = Flask(__name__)

# camera = ('rtsp://admin@192.168.21.220:554/ch0_0.264')  # use 0 for web camera
# #  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera
# # for local webcam use cv2.VideoCapture(0)

# def gen_frames():  # generate frame by frame from camera
#     while True:
#         # Capture frame-by-frame
#         success, frame = camera.read()  # read the camera frame
#         if not success:
#             break
#         else:
#             ret, buffer = ('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


# @app.route('/video_feed')
# def video_feed():
#     #Video streaming route. Put this in the src attribute of an img tag
#     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/')
# def index():
#     """Video streaming home page."""
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

import cv2 
# video = cv2.VideoCapture(0)
video = cv2.VideoCapture('rtsp://admin:admin123@192.168.21.102:554/stream?mode=real&idc=1&ids=1')

while True:
    _,frame =video.read()
    cv2.imshow("IP Camera Video Streaming", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
