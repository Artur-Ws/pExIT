
imiona = ['Adam', 'Stanisław', 'Maria', 'Zofia', 'Mikołaj']

n = 1

for imie in imiona:
    print(str(n) + ". " + imie)
    n += 1

for n, imie in enumerate(imiona, 1):
    print(n, imie)


A = [1, 1, 4, 9]

for n, num in enumerate(A):
    print(n, num)