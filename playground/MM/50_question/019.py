def dodaj_do_listy_1(n, lista=[]):
    lista.append(n)
    print(lista)


dodaj_do_listy_1(1)
dodaj_do_listy_1(2, [4, 5])
dodaj_do_listy_1(3)


def dodaj_do_listy_2(n, lista=None):

    if lista is None:
        lista = []

    lista.append(n)
    return lista


print(dodaj_do_listy_2(1))
print(dodaj_do_listy_2(2, [4, 5]))
print(dodaj_do_listy_2(3))
