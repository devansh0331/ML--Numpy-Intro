import numpy as np

# For 1-D array
print("For 1-D array")
a = np.array([1,2,3,4,5,6])
print(a[2:5])

# For 2-D array
print("For 2-D array")
a = np.array([[6,7,8] , [1,2,3] , [9,5,4]])
print(a[1:3])
print(a[0 , 1]) # Accessing 7
print(a[0:2]) # Accessing 1st two rows
print(a[ : , 2]) # Accessing 2nd column
print(a[ : , 1:3]) # Accessing last two columns

# Iterating through arrays
a = np.arange(15).reshape((5,3))
print(a)
for item in a:
    for ele in item:
        print(ele)

for cell in a.flat:
    print(cell)

# NOTE : You can also use nditer funtion for better iterating experience

print(np.nditer(a))

for x in np.nditer(a , order='C'):
    print(x)
for x in np.nditer(a , order='F'):
    print(x)

# Stacking of array
a1 = np.arange(0,6).reshape(3,2) 
a2 = np.arange(6,12).reshape(3,2) 
print(a1 , a2)
print(np.vstack((a1,a2)))
print(np.hstack((a1,a2)))

# Splitting of array
a = np.arange(26).reshape(2,13)
print(a)
print(np.hsplit(a,13))
print(np.vsplit(a,2))

# Indexing with boolean array
a = np.arange(9).reshape(3,3)
b = a > 5
print(b)
print(a[b])