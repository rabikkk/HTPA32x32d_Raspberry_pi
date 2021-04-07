import numpy as np
import cv2
from htpa import *
import pickle
i = 0
k=0
dev = HTPA(0x1A)

while(True):
	# ~ print("Capturing image " + str(i))
	if (i == 5):
		dev.measure_observed_offset()

	(pixel_values, ptats) = dev.capture_image()
	im = dev.temperature_compensation(pixel_values, ptats)
	im = dev.offset_compensation(im)
	im = dev.sensitivity_compensation(im)

	# resize and scale image to make it more viewable on raspberry pi screen
	im = cv2.resize(im, None, fx=12, fy=12)	
	im -= np.min(im)
	im /= np.max(im)
	
	imcolor = np.uint8(255 * im)
	if k==15:
		np.save('data1.npy',im)
		np.save('ptats.npy',pixel_values)
		cv2.imwrite("image.png",imcolor)
	k=k+1
	imcolor=cv2.applyColorMap(imcolor,cv2.COLORMAP_JET)

	cv2.imshow('frame', im)
	cv2.imshow('frame1', imcolor)
	
	i += 1

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

dev.close()

cv2.destroyAllWindows()
