#Exercise 1. Create an array from a list
import numpy as np
x = range(1,11)
a1 = np.array(x, np.int32)
a2 = np.array(x, np.float32)
print a1.dtype
print a2.dtype

#Exercise 2. Create an array in different ways
b1 = np.zeros((2,3,4)) #createssizeofarray
b2 = np.ones((2,3,4))
b3 = np.arange(1000) #arrayrangefunction
print b1
print b2

#Exercise 3. Indexing and slicing arrays
c1 = [2, 3.2, 5.5, -6.4, -2.2, 2.4]
print c1[1]
print c1[1:4]
c2 = np.array((c1, [1, 22, 4, 0.1, 5.3, -9], [3, 1, 2.1, 21, 1.1, -2]))
print c2[:, 3]
print c2[1:4, 0:4]
print c2[1:, 2]

