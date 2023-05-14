import numpy as np

arr = np.array([1,2,3,4,5,6] , dtype="float")
print(arr)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
print(arr.itemsize)

arr2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr2d.ndim)
print(arr2d.size)

# np.zeros
print(np.zeros((3,4)))

# np.ones
print(np.ones((5,6)))

# np.arange()
arr = np.arange(10)
arr = np.arange(1,10)
arr = np.arange(1,10,2)
print(arr)

# np.linspace()
arr = np.linspace(1,5,10)
print(arr)

# reshape((x,y))
arr = np.array([[1,2],[3,4],[5,6]])
print(arr.shape)
arr = arr.reshape(2,3)
print(arr)

# ravel()
print(arr.ravel())

# min()
print(arr.min())

# max()
print(arr.max())

# sum()
print(arr.sum())
print(arr.sum(axis=0))
print(arr.sum(axis=1))

# sqrt()
print(np.sqrt(arr))

# std()
print(np.std(arr))

# Operations on two arrays
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

