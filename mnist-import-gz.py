#Adapted from: 
#	https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

#import gzip library
import gzip
import numpy as np

# dataPath = 'data/train-labels-idx1-ubyte.gz'
# dataPath = 'data/train-images-idx3-ubyte.gz'

# def read_labels_from_file(fPath):
	# with gzip.open(fPath, 'rb') as f:
		# mNum= f.read(4)
		# mNum = int.from_bytes(mNum, 'big')
		# print("Magic number: ", mNum)
		
		# nolab = f.read(4)
		# nolab = int.from_bytes(nolab, 'big')
		# print("Label amount: ", nolab)
		
		# labels = [f.read(1) for i in range(nolab)]
		# labels = [int.from_bytes(label, 'big') for label in labels]
		
		# return labels
	# f.close()
	
# train_labels = read_labels_from_file('data/train-labels-idx1-ubyte.gz')
# test_labels = read_labels_from_file('data/t10k-labels-idx1-ubyte.gz')


def read_images_from_file(fPath):
	with gzip.open(fPath, 'rb') as f:
		mNum= f.read(4)
		mNum = int.from_bytes(mNum, 'big')
		print("Magic number: ", mNum)
		
		imgNum = f.read(4)
		imgNum = int.from_bytes(imgNum, 'big')
		print("Image amount: ", imgNum)
		
		noRows = f.read(4)
		noRows = int.from_bytes(noRows, 'big')
		print("Row number: ", noRows)
		
		noCols = f.read(4)
		noCols = int.from_bytes(noCols, 'big')
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

def print_image(i):
	for r in train_images[i]:
		for col in r:
			print('.' if col < 127 else '#', end='')
		print()	
		
print_image(5)

import PIL.Image as pil
img = train_images[5]
img = np.array(img)
img = pil.fromarray(img)
img = img.convert('RGB')
img.show()
img.save('2.png')
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

