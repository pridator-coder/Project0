import numpy as np
a = np.array([1,2,3], dtype='int16')
print(a)

b = np.array([[9.0,8.0,7.0], [6.0,5.0,4.0], [3.0,2.0,1.0]])
print(b)

# Get Dimension
print(a.ndim)

# Get Shape
print(a.shape)
print(b.shape)
print(a.dtype)
print(a.itemsize)
# Get Total size
print(a.size*a.itemsize)
print(a.nbytes)

c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(c)

# get a specific element
print(c[1,5])

# get a specific row
print(c[0, :])
# : means all the columns here
print(c[:, 2])

# getting a bit fancy [row, starting index:final index(excluded):step]
print(c[0, 1:6:2])
print(c[0, 1:-1:2])

# changing an element
c[1,5] = 20
print(c[1,5])

# to change a complete column
c[:,2] = 5
print(c)

# 3-d example
d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(d)
# to get an element in this for ex 4 (works outside in)
d[0,1,1] = 9
print(d[0,1,1])

# replace

d[:,1,:]=[9,9]
print(d)

# initial different types of arrays

# all zeros matrix

print(np.zeros((2)))
print(np.zeros((2,2)))
print(np.zeros((2,2,3)))
print(np.zeros((2,2,3,4)))

#All 1s matrix

print(np.ones((4,3,2)))

#ANy other number
print(np.full((2,2), 99, dtype='float32'))


