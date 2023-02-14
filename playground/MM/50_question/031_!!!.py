nazwiska = ['jan kot', 18, 'ANNA KRÓL', 'jÓzef BYK', ['nie', 'wasza', 'sprawa'], 'ROBERT wąŻ']


def filterer(lista):
    n = 0

    for i in lista:

        if type(lista[n]) is not str:

            lista.remove(i)

        n += 1

    return lista


def uppercaser(lista):

    lista_upper = []

    for i in lista:

        n = str(i).title()

        lista_upper.append(n)
    return lista_upper


# print(filterer(nazwiska))
# print(uppercaser(nazwiska))

nazwiska_wyczyszczone = list(filter(lambda x: type(x) is str, nazwiska))
print(nazwiska_wyczyszczone)

nazwiska_poprawione = list(map(lambda x: x.lower().title(), nazwiska_wyczyszczone))

print(nazwiska_poprawione)
