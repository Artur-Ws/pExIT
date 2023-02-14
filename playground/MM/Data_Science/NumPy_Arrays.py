import numpy as np


my_list = [1, 2, 3]
arr = np.array(my_list)     # Zamienia listę w wektor

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

arr_2 = np.array(my_mat)    # Zamienia listę list w macierz

arr_3 = np.arange(0, 11, 2)     # Tworzy wektor od 0 do 10 ze skokiem co 2

print(my_mat)
print("")
print(arr_2)
print("")
print(arr_3)
print("")

arr_4 = np.zeros(3)     # Tworzy wektor z 3 zer

arr_5 = np.zeros((5, 5))        # Tworzy macierz 5x5 z samych zer (tupla w środku, 1 arg to ilość wierszy, 2 to ilość kolumn)

print(arr_4)
print("")
print(arr_5)
print("")
print(type(arr))
print("")
print(type(my_mat))
print("")

arr_6 = np.ones(10)     # Tworzy tablicę z 10 jedynek
arr_7 = np.ones((3, 4))     # Tworzy macierz z jedynek o wymiarach 3 x 4

print(arr_6)
print("")
print(arr_7)
print("")

arr_8 = np.linspace(0, 5, 15)       # Tworzy wektor złożony z 15 równomiernie rozłożonych elementów w zakresie od 0 do 5

print(arr_8)
print("")

list_8 = list(arr_8)

print(list_8)
print("")

arr_9 = np.eye(4)       # Tworzy macierz jednostkową (macierz kwadratowa złożona z 1 na głównej przekątnej i 0) o wymiarach 4 x 4

print(arr_9)
print("")

arr_10 = np.random.rand(5)      # Tworzy wektor z losowych liczb od 0 do 1 złożony z 5 wartości

print(arr_10)
print("")

arr_11 = np.random.rand(5, 5)      # Tworzy macierz 5 x 5 z losowych liczb od 0 do 1

print(arr_11)
print("")

arr_12 = np.random.randn(2)      # Tworzy wektor z losowych liczb z rozkłądu Gausa złożony z 2 wartości

print(arr_12)
print("")

arr_13 = np.random.randn(4, 4)      # Tworzy macierz 4 x 4 z losowych liczb z rozkładu Gausa

print(arr_13)
print("")

arr_14 = np.random.randint(1, 100, 10)      # Tworzy wektor z 10 losowych intigerów z przedziału od 9 do 99

print(arr_14)
print("")

arr_15 = np.arange(25)

print(arr_15)
print("")

ranarr = np.random.randint(0, 50, 10)

print(ranarr)
print("")

print(arr_15.reshape(5, 5))     # Zmienia wymiary wektora arr_15 (Wymiary muszą być zg dne z ilością elementów bazowej talbicy (macierzy lub wektora)

print(ranarr.max())
print(ranarr.min())

print(ranarr.argmax())      # Podaje lokalizacje największej wartości z wektora ranarr
print(ranarr.argmin())      # Podaje lokalizacje njamniejszą wartości z wektora ranarr
print(ranarr.shape)     # Podaje informacje o kształcie tablicy

ranarr = ranarr.reshape(2, 5)

print(ranarr)
print(ranarr.shape)
print(ranarr.dtype)     # Podaje informacje o typie danych w tablicy
