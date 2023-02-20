import numpy as np

arr_1 = np.arange(0, 11)

print(arr_1)
print(arr_1 + arr_1)    # Dodano 2 wektory do siebie
print(arr_1 - arr_1)    # Odjęto 2 wektory do siebie
print(arr_1 * arr_1)    # Pomnożono 2 wektory przez siebie
print(arr_1 + 100)      # Dodano 100 do wektora
print(arr_1 ** 2)       # wektor podniesiony do kwadratu

print(np.sqrt(arr_1))

print(np.exp(arr_1))


arr_2 = np.arange(1,11)

print(arr_2 / arr_2)    # Podzielono 2 wektory przez siebie (trzeba było stworzyć nowy wektor, który zaczyna się od 1, nie można dzielić rpzez 0!)
