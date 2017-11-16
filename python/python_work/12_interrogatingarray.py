# Exercise 1. Interrogate an array
import numpy as np
arr = np.array([range(4), range(10,14)])
print arr.shape(2, 4)
print arr.size
print arr.min()
print arr.max()

# Exercise 2. Generate new arrays from modigying
print np.reshape(arr, (2, 2, 2))
print np.transpose(arr) #transposed
print np.ravel(arr) #flatten to single dimension
print arr.astype(np.float64) #conver to floats


