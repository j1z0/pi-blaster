from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

print("create the camera")
with PiCamera() as camera:
	camera.resolution = (640, 480)
	camera.framerate = 16 
	rawCapture = PiRGBArray(camera, size=(640,480))
        camera.CAPTURE_TIMEOUT = 3


	print("start up camera")
	#allow camera to warmup
	time.sleep(1)
	print("start the loop")

	for frame in camera.capture_continuous(rawCapture, format="bgr", use_vide_port=True):
		print("in the loop")
		#grap the raw NumPy array repr the image
		image = frame.array

		print("in the loop with frame")

		#show the frame
		cv2.imshow("Frame", image)
		key = cv2.waitKey(1) & 0xFF

		#clear the stream in prep for the next frame
		rawCapture.truncate(0)

		print(key)
		if key == ord("q"):
		    break

print "all done";


