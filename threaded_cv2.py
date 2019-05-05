from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2
from servoctrl import Servo

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=1,
	help="Whether or not frames should be displayed")
args = vars(ap.parse_args())

#start the servo
servo = Servo(18)
servo.move(90)

# created a *threaded* video stream, allow the camera sensor to warmup,
# and start the FPS counter
print("[INFO] sampling THREADED frames from webcam...")
vs = WebcamVideoStream(src=0).start()

#load face detection stuff
faceCascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

fps = FPS().start()
 
# loop over some frames...this time using the threaded stream
while fps._numFrames < args["num_frames"]:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#perform face detection
	faces = faceCascade.detectMultiScale(
	    frame,
	    #gray,
	    scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
	)
	for (x, y, w, h) in faces:
		#    	print("x=%s, y=%s, w=%s, h=%s" % (x,y,w,h))
		#x, y, w, h = faces
		xpos = x - (w/3)
		#roughly 140-180 is middle
		#so split in the middle and remove the
		if not (xpos >= 140 and xpos <=180):
			xdist = xpos - 160
			print(xpos)
			print(xdist)
			xdist = xdist / 15.0
			if xdist > 0:
			    servo.adjust(xdist)
			    print("move right")
			else:
			    servo.adjust(xdist)
			    print("move left")
			#move_servo(xdist)
		break
		
	# check to see if the frame should be displayed to our screen
	if args["display"] > 0:
		#rectangle for detected face
		for (x,y, w, h) in faces:
		    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
 
	# update the FPS counter
	fps.update()
 
# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
servo.shutdown()
