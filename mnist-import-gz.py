#Adapted from https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

#import gzip library
import gzip

f = gzip.open('data/train-labels-idx1-ubyte.gz', 'rb')
firstByte = f.read(1)
print(firstByte)
f.close()