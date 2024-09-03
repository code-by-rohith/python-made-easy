import numpy as np

# Creating array object
arr = np.array( [[ 1, 2, 3],
                 [ 4, 2, 5]] )


arr1 = np.arange(4, dtype = np.float_).reshape(2, 2)

print("Array is of type: ", type(arr))
print(arr1)

print("No. of dimensions: ", arr.ndim)


print("Shape of array: ", arr.shape)

print("Size of array: ", arr.size)

print("Array stores elements of type: ", arr.dtype)