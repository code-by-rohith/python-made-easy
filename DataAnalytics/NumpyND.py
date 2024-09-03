import numpy as np

#creation

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
e = np.array([1, 2, 3, 4], ndmin=5)

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(e.ndim)


#indexing
print("5d array ",e[0][0][0][0][3])
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("indexing ",arr[1,4])
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("indexing ",arr[0, 1, 2])

#negative indexing
arr = np.array([[1,2,3,-4,-5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[0, -2])

#slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("slicing ",arr[0:5])

#negative slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("negative slicing", arr[-3:-1])

print(arr[1:5:2])
print(arr[::2])

#Slicing 2D Array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],  [11, 12, 13, 14, 15]])
print("ARRAY",arr[:2, 1:4])
print("arr 2d Slice", arr[0:3, 1])
print("arr 2d Slice flatten", arr[0:3, 1:3])

#data types
arr = np.array([1, 2, 3, 4])
print("type ",arr.dtype)
arr = np.array(['apple', 'banana', 'cherry'])
print("type ",arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

#Copy and View

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)


arr = np.array([1, 2, 3, 4, 5])
y = arr.view()
arr[0] = 42
print(arr)
print(y)

print(x.base)
print(y.base)

#Shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

#Reshape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
newarr = arr.reshape(2, 3, 2)
print(newarr)

#iteration
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)

for x in arr:
  for y in x:
    print(y)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  for y in x:
    print("2d " ,y)
    for z in y:
      print("3d ", z)

#nditer

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print("Recent",x)

#joins

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
++
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=0)
print(arr)


