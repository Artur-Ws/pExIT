import numpy as np

# Arrays creation:
# Task 1
arr_1 = np.zeros(10)
print(arr_1)
print()

# Task 2
arr_2 = np.ones(10)
print(arr_2)
print()

# Task 3
arr_3 = np.ones(10) * 5
print(arr_3)
print()

# Task 4
arr_4 = np.arange(10, 51)
print(arr_4)
print()

# Task 5
arr_5 = np.arange(10, 51, 2)
print(arr_5)
print()

# Task 6
arr_6 = (np.arange(0, 9)).reshape(3, 3)
print(arr_6)
print()

# Task 7
arr_7 = np.eye(3)
print(arr_7)
print()

# Task 8
arr_8 = np.random.rand(1)
print(arr_8)
print()

# Task 9
arr_9 = np.random.randn(25)
print(arr_9)
print()

# Task 10
arr_10 = np.linspace(0.01, 1, 100).reshape(10, 10)
print(arr_10)
print()

# Task 11
arr_11 = np.linspace(0, 1, 20)
print(arr_11)
print()

# Arrays indexing and selection:

mat = np.arange(1, 26).reshape(5, 5)
print(mat)
print()

# Task 1
slice_mat_1 = mat[2:, 1:]
print(mat)
print()
print(slice_mat_1)
print()

# Task 2
slice_mat_2 = mat[3, 4]
print(mat)
print()
print(slice_mat_2)
print()

# Task 3
slice_mat_3_1 = np.array([[mat[0, 1]], [mat[1, 1]], [mat[2, 1]]])
slice_mat_3_2 = mat[:3, 1:2]
print(type(slice_mat_3_1))
print(type(slice_mat_3_2))
print(mat)
print()
print(slice_mat_3_1)
print(slice_mat_3_2)
print()

# Task 4
slice_mat_4 = mat[4]
print(mat)
print()
print(slice_mat_4)
print()

# Task 5
slice_mat_5 = mat[3:]
print(mat)
print()
print(slice_mat_5)
print()

# Arrays operations:

# Task 1
sum_mat = np.sum(mat)
print(mat)
print()
print(sum_mat)
print()

# Task 2
std_mat = np.std(mat)
print(mat)
print()
print(std_mat)
print()

# Task 3
col_sum_mat = np.sum(mat, axis=0)
print(mat)
print()
print(col_sum_mat)
print()
