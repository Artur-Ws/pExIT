import numpy as np

arr_1 = np.arange(0, 11)

print(arr_1)
print(arr_1[8])
print(arr_1[0:5])
print(arr_1[:6])
print(arr_1[5:])

arr_1[0:5] = 100        # Zamienia wartości o ideksach 0, 1, 2, 3 i 4 na 100
print(arr_1)

arr_2 = np.arange(0, 11)

slice_of_arr_2 = arr_2[0:6]     # Tworzy odniesienie (a nie kopie) do części wektora arr_2
print(slice_of_arr_2)

slice_of_arr_2[:] = 99      # Zamienia odniesienie arr_2 przypisane do zmiennej slice_of_arr_2 na 99
print(slice_of_arr_2)
print(arr_2)

arr_2_copy = arr_2.copy()

arr_2_copy[:] = 100

print(arr_2_copy)
print(arr_2)

print("")
print("")
arr_3 = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_3)

print("")
print(arr_3[0])
print("")
print(arr_3[0][0])
print("")
print(arr_3[2][1])
print(arr_3[2, 1])

print("")
print(arr_3[:2, 1:])
print("")
print(arr_3[1:, :2])

arr_4 = np.arange(1, 21)
print(arr_4)
print(arr_4 > 5)

bool_arr = arr_4 > 5
print(bool_arr)

print(arr_4[arr_4 < 8])

print("")
arr_5 = np.arange(1, 51).reshape(5, 10)
print(arr_5)

print("")
print(arr_5[1:3, 4:6])
