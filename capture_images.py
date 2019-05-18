"""
Capture images and save them to disk
"""

import time
from picamera import PiCamera


def capture_image(save_folder):
	camera = PiCamera()
	camera.resolution = (1024, 768)
	camera.framerate = 5


	time.sleep(2)


def a(number):
	o = number * 5
	return o

if __name__ == '__main__':
	a(5)
	
