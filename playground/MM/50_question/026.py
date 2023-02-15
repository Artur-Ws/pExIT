file = "moj_plik.txt"

lista = []

with open("moj_plik.txt", 'w') as f:

    for n in range(1, 101):
        f.write(str(n) + '\n')

with open("moj_plik.txt", "r") as f:

    for line in f:
        lista.append(int(line.rstrip()))

print(lista)


with open("przeczytaj_mnie.txt", 'r', encoding='utf-8') as f:
    print(f.read())

