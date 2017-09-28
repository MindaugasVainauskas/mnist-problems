#Adapted from: 
#	https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

#import gzip library
import gzip
import struct

#dataPath = 'data/train-labels-idx1-ubyte.gz'
dataPath = 'data/train-images-idx3-ubyte.gz'

def read_labels_from_file(fPath):
	with gzip.open(fPath, 'rb') as f:
		mNum= f.read(4)
		mNum = int.from_bytes(mNum, 'big')
		print("Magic number: ", mNum)
		
		nolab = f.read(4)
		nolab = int.from_bytes(nolab, 'big')
		print("Label amount: ", nolab)
		
		labels = [f.read(1) for i in range(nolab)]
		labels = [int.from_bytes(label, 'big') for label in labels]
		
		return labels
	
train_labels = read_labels_from_file('data/train-labels-idx1-ubyte.gz')
test_labels = read_labels_from_file('data/test-labels-idx3-ubyte.gz')

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

