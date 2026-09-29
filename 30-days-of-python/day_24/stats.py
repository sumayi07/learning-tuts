# Day 24

#pip install numpy, matplotlib, seaborn

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

nums = [1, 2, 3, 4, 5]
print("Type:", type(nums))
print(nums)

numpy_nums = np.array(nums)
print(type(numpy_nums))
print(numpy_nums)

float_nums = np.array(nums, dtype = float)
print(type(numpy_nums))
print(float_nums)

bool_array = np.array([0, 1, -1, 0, 0], dtype = bool)
print(type(bool_array))
print(bool_array)

two_d_numpy = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(type(two_d_numpy))
print(two_d_numpy)

np_to_list = numpy_nums.tolist()
print(type(np_to_list))
print("one dimensional array: ", np_to_list)
print("two dimensional array: ", two_d_numpy.tolist())

tpl = (1, 2, 3, 4, 5)
print(type(tpl))
print("python_tuple: ", tpl)

numpy_tpl = np.array(tpl)
print(type(numpy_tpl))
print("numpy array from tuple: ", numpy_tpl)

print(numpy_nums)
print("shape: ", numpy_nums.shape)
print(two_d_numpy)
print("shape: ", two_d_numpy.shape)
print("size: ", two_d_numpy.size)

three_d_numpy = np.array([[[1,2,3],[4,5,6],[7,8,9]], [[1,2,3],[4,5,6],[7,8,9]], [[1,2,3],[4,5,6],[7,8,9]]])
print(three_d_numpy)
print(three_d_numpy.shape)

print(numpy_nums)
print(numpy_nums.dtype)
print(float_nums)
print(float_nums.dtype)

print(numpy_nums)
print(numpy_nums.size)

print(numpy_nums + 10)

print(numpy_nums - 10)

print(numpy_nums * 10)

print(numpy_nums / 10)

print(numpy_nums % 3)

print(numpy_nums // 10)

print(numpy_nums ** 2)

print(np.array(float_nums, dtype = int))

first_row = two_d_numpy[0]
second_row = two_d_numpy[1]
third_row = two_d_numpy[2]
print("first row: ", first_row)
print("second row: ", second_row)
print("third row: ", third_row)

first_col = two_d_numpy[:,0]
second_col = two_d_numpy[:,1]
third_col = two_d_numpy[:,2]
print("first col: ", first_col)
print("second col: ", second_col)
print("third col: ", third_col)

first_two_row_and_col = two_d_numpy[0:2, 0:2]
print(first_two_row_and_col)

print("reversed", two_d_numpy[::-1, ::-1])

numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
print(numpy_zeroes)

first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)

flattened = reshaped.flatten()
print(flattened)

np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print(np_list_one + np_list_two)
print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))

print(np.random.random())
print(np.random.random(5))

print(np.random.randint(0,11))
print(np.random.randint(2, 10, size = 4))

normal_array = np.random.normal(79, 15, 80)
print(normal_array)

print(sns.set())
print(plt.hist(normal_array, color="grey", bins=50))

four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)

whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)

print(np.linspace(1.0, 5.0, num=10))
print(np.linspace(1.0, 5.0, num=10, endpoint=False))

print(np.logspace(2, 4.0, num=4))

x = np.array([1,2,3], dtype=np.complex128)
print(x)
print(x.itemsize) #prints size in bytes

np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
## min, max, mean, median, sd
print('min: ', np_normal_dis.min())
print('max: ', np_normal_dis.max())
print('mean: ',np_normal_dis.mean())
# print('median: ', np_normal_dis.median())
print('sd: ', np_normal_dis.std())

print(two_d_numpy)
print('Column with minimum: ', np.amin(two_d_numpy,axis=0))
print('Column with maximum: ', np.amax(two_d_numpy,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_d_numpy,axis=1))
print('Row with maximum: ', np.amax(two_d_numpy,axis=1))

a = [1,2,3]

# Repeat whole of 'a' two times
print('Tile:   ', np.tile(a, 2))

# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))

f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
print(np.dot(f, g))  # 23

h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
np.matmul(h, i)
np.linalg.det(i)
