import numpy as np
import time
import sys



# arr = np.array([1,2,3,4,5])
# arr = np.arange(100)
# print(arr)

# Numpy vs Python List

# Taking less space
'''
l = range(1000)
arr = np.arange(1000)
print(sys.getsizeof(5)*len(l)) # 28000 bytes
print(arr.size*arr.itemsize) # 4000 bytes
'''

# Faster
size = 100000

l1 = range(size)
l2 = range(size)

start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print("Time taken by python list : " ,(time.time() - start)*1000) # 11.083602905273438 ms

a1 = np.arange(size) 
a2 = np.arange(size) 

start = time.time()
result = a1 + a2
print("Time taken by numpy array : " , (time.time() - start)*1000) # 1.0280609130859375 ms


