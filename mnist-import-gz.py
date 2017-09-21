#Adapted from: 
#	https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

#import gzip library
import gzip

#dataPath = 'data/train-labels-idx1-ubyte.gz'
dataPath = 'data/train-images-idx3-ubyte.gz'

f = gzip.open(dataPath, 'rb')
bytes = f.read(4)
print(bytes)
#Adapted from:
#	https://docs.python.org/3/library/stdtypes.html#int.from_bytes
x = int.from_bytes(bytes, byteorder = 'big')
print("Big endian decoded value: %d" % (x))

y = int.from_bytes(bytes, byteorder = 'little')
print("Little endian decoded value: %d" % (y))
f.close()