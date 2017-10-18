# Mindaugas Vainauskas
# Year 4 SW Development course
# Emerging Technologies module
# GMIT 2017

#import libraries needed
import gzip
import numpy as np
import struct
import PIL.Image as pil

def read_labels_from_file(fPath):
	with gzip.open(fPath, 'rb') as f:
	
		#This line is adapted from
		#https://gist.github.com/akesling/5358964#file-mnist-py-L26
		mNum, labNum = struct.unpack(">II", f.read(8))		
		print("Magic number: ", mNum)		
		print("label count: ", labNum)	
		
		labels = f.read(labNum)	
		return labels
	f.close()

def read_images_from_file(fPath):
	with gzip.open(fPath, 'rb') as f:
	
		#This line is adapted from
		#https://gist.github.com/akesling/5358964#file-mnist-py-L26
		#Reason being it writes out data in single line instead of 8
		mNum, imgNum, noRows, noCols = struct.unpack(">IIII", f.read(16))
		
		print("Magic number: ", mNum)		
		print("Image amount: ", imgNum)		
		print("Row number: ", noRows)		
		print("Column number: ", noCols)	

		#Adapted from(For a massive speed of processing increase!)
		#https://gist.github.com/ischlag/41d15424e7989b936c1609b53edd1390
		#I needed to do this as my laptop was taking over 5 minutes to return results of image processing.
		buffer = f.read(noRows * noCols * imgNum)
		images = np.frombuffer(buffer, dtype=np.uint8).astype(np.float32)
		images = images.reshape(imgNum, noRows, noCols, 1)
		
	return images
	f.close()
	
# Get the image and label sets from data folder
label_set = read_labels_from_file('data/train-labels-idx1-ubyte.gz')
image_set = read_images_from_file('data/train-images-idx3-ubyte.gz')

# Print image on the console
def print_image(i):
	for r in image_set[i]:
		for col in r:
			print('.' if col < 127 else '#', end='')
		print()		
	print(label_set[i])



#For image saving and rendering I adapted code from:
#https://stackoverflow.com/questions/34324958/trying-to-create-noise-image-with-noise-numpy-and-image
def save_image(i):
	img = image_set[i]
	img = np.asarray(img, dtype=np.float32)
	img = pil.fromarray((img)**16, mode='RGBA').convert('L', dither = pil.NONE)
	img.show()
	img.save('./images/train-%d-%d.png' % (i, label_set[i]))
	
#define function to print and save images in range
def print_save_range(i, j):
	for e in range(i, j):
		print_image(e)
		save_image(e)
	
imCount = 60000
#Calls to functions	
print()
print("Enter range of images to show. Enter same number as first and last number to print single image!")
print("Numbers must be in ascending order or equal")
#check for valid/invalid input before assigning first/last numbers in range
while 1:
	startRange = int(input("Enter first number in range: "))
	if startRange >= 0 and startRange < imCount:
		break
		
while 1:
	endRange= int(input("Enter last number in range: "))
	if endRange >= startRange and endRange < imCount:
		break
		
endRange = endRange+1

#run the rendering for given range of images
print_save_range(startRange, endRange)	