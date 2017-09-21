#Adapted from https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

#import gzip library
import gzip

#dataPath = 'data/train-labels-idx1-ubyte.gz'
dataPath = 'data/train-images-idx3-ubyte.gz'

f = gzip.open(dataPath, 'rb')
firstByte = f.read(4)
print(firstByte)
f.close()