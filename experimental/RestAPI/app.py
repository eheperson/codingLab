from flask import Flask 
from flask import redirect
from flask import Response
from flask import url_for 
from flask import render_template
from flask import request 
#
from camera import VideoCamera
#
import time
import threading
import os
#
#
#Create flask web app
app = Flask(__name__)
#
@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here
#
@app.route('/machine')
def machine():
    return render_template('index.html') #you can customze index.html here
#
@app.route('/about')
def about():
    return render_template('about.html') #you can customze index.html here
#
@app.route("/main", methods=["POST", "GET"])
def main():
    return "hello motherfucker"
## ---                                                                              
## -----------------------------Video Stream - Begin --------------------------------------- ##
## ---
pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.
#
@app.route('/videoStream')
def streamer():
    return render_template('stream.html')
#
def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#
@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
#
## ---                                                                              
## -----------------------------Video Stream - End --------------------------------------- ##
## ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)

