"""
NumPy is used to work with arrays. The array object in NumPy is called ndarray.
We can create a NumPy ndarray object by using the array() function.

        ndarray.ndim     : The number of axes (dimensions) of the array.

        ndarray.shape    : The dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension.
                        For a matrix with n rows and m columns, shape will be (n,m). The length of the shape tuple is therefore the number of axes, ndim.

        ndarray.size     :  The total number of elements of the array. 
                            This is equal to the product of the elements of shape.

        ndarray.dtype    : An object describing the type of the elements in the array. 
                        One can create or specify dtype’s using standard Python types. 
                        Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.

        ndarray.itemsize : The size in bytes of each element of the array. 
                        For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). 
                        It is equivalent to ndarray.dtype.itemsize.

        ndarray.data     : The buffer containing the actual elements of the array. 
                        Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.
"""
#
import numpy as np
print(np.__version__)
#
# Use a array to create a NumPy array:
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
#
# Use a tuple to create a NumPy array:
arr2 = np.array((11, 22, 33, 44, 55))
print(arr2)
print(type(arr2))
#
#-----------------------------------------------------------------------------------------------------
## 0-D arrays
#
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
arr0d = np.array(42)
print(arr0d)
#-----------------------------------------------------------------------------------------------------
#
#-----------------------------------------------------------------------------------------------------
## 1-D arrays
#
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d)
#
print(arr1d[2] + arr1d[3])
#-----------------------------------------------------------------------------------------------------
#
#-----------------------------------------------------------------------------------------------------
## 2-D arrays
#
# An array that has 1-D arrays as its elements is called a 2-D array.
# These are often used to represent matrix or 2nd order tensors.
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
#
print('2nd element on 1st dim: ', arr2d[0, 1])
#-----------------------------------------------------------------------------------------------------
#
#-----------------------------------------------------------------------------------------------------
## 3-D arrays
#
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# These are often used to represent a 3rd order tensor.
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3d)
#
print(arr3d[0, 1, 2])
#-----------------------------------------------------------------------------------------------------
#
#-----------------------------------------------------------------------------------------------------
## Higher Dimensional Arrays
#
# An array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by using the ndmin argument.
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
#-----------------------------------------------------------------------------------------------------
#
#-----------------------------------------------------------------------------------------------------
## Check Number of Dimensions?
#
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)   
#-----------------------------------------------------------------------------------------------------

