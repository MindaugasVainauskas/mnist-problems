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

		images = []
		
		for i in range(imgNum):
			rows = []
			for r in range(noRows):
				cols = []
				for c in range(noCols):
					cols.append(int.from_bytes(f.read(1), 'big'))
				rows.append(cols)
			images.append(rows)
		
	return images
	f.close()
	
train_images = read_images_from_file('data/train-images-idx3-ubyte.gz')
#test_images = read_images_from_file('data/t10k-images-idx3-ubyte.gz')

#Set selected image nuumber. Easier than looking where to change it when need to render different one.
selectedImage = 3

def print_image(i):
	for r in train_images[i]:
		for col in r:
			print('.' if col < 127 else '#', end='')
		print()	
		
print_image(selectedImage)

import PIL.Image as pil
img = train_images[selectedImage]
img = np.array(img)
img = pil.fromarray(img)
img = img.convert('RGB')
img.show()
img.save('Image_%s.png', selectedImage)
# f.close()
# f = gzip.open(dataPath, 'rb')
# bytes = f.read(8)
# print(bytes)
# Adapted from:
	# https://docs.python.org/3/library/stdtypes.html#int.from_bytes
# x = int.from_bytes(bytes, byteorder = 'big')
# print("Big endian decoded value: %d" % (x))

# y = int.from_bytes(bytes, byteorder = 'little')
# print("Little endian decoded value: %d" % (y))

# print(struct.unpack('>II', bytes))

