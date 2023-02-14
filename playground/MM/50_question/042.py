P = [-10, -7, -5, -3, 0, 3, 5, 21, 68, 341, 500]

# print(341 in P)

szukana = 341
lewy = 0
prawy = len(P) - 1

while lewy <= prawy:

    srodkowy = (lewy + prawy) // 2

    if P[srodkowy] == szukana:
        print(f"Liczba {szukana} znajduje sie na liście!!")

        break

    elif P[srodkowy] < szukana:
        lewy = srodkowy + 1

    else:
        prawy = srodkowy -1

else:
    print(f"Liczby {szukana} nie ma na liście...")