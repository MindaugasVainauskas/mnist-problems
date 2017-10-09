#Adapted from: 
#	https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

#import gzip library
import gzip
import numpy as np
import struct

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

		# images = []
		
		# for i in range(imgNum):
			# rows = []
			# for r in range(noRows):
				# cols = []
				# for c in range(noCols):
					# cols.append(int.from_bytes(f.read(1), 'big'))
				# rows.append(cols)
			# images.append(rows)
		
	return images
	f.close()
	
train_images = read_images_from_file('data/train-images-idx3-ubyte.gz')

#test_images = read_images_from_file('data/t10k-images-idx3-ubyte.gz')

#Set selected image nuumber. Easier than looking where to change it when need to render different one.
selectedImage = int(input("Which image to show?: "))

def print_image(i):
	for r in train_images[i]:
		for col in r:
			print('.' if col < 127 else '#', end='')
		print()		


print("Selected image on screen was %s:" % selectedImage)

#For image saving and rendering I adapted code from:
#https://stackoverflow.com/questions/34324958/trying-to-create-noise-image-with-noise-numpy-and-image
import PIL.Image as pil

def save_image(i):
	img = train_images[i]
	img = np.asarray(img)
	img = pil.fromarray(img, mode='RGBA')
	img.show()
	img.save('./images/Image_%d.png' % i)
	
#define function to print and save images in range
def print_save_range(i, j):
	for e in range(i, j):
		print_image(e)
		save_image(e)
	
#Calls to functions	
print_image(selectedImage)
save_image(selectedImage)
# print("Enter range of images to show. Enter same number as first and last number to print single image!")
# print("Numbers must ne in ascending order or equal")
# startRange = int(input("Enter first number in range: "))
# endRange= int(input("Enter last number in range: "))
# endRange = endRange+1

# print_save_range(startRange, endRange)

	
	
	
	
	
	
	