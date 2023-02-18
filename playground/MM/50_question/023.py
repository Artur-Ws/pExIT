lambda x: x + 2


L = [("Anna", 82), ("Robert", 33), ("Artur", 40), ("Feliks", 56)]
L_posortowana = sorted(L, key=lambda x: x[1])
print(L_posortowana)


S = ['Anna', 'Robert', 'Artur', 'Feliks']

S_posortowana = sorted(S, key=lambda x: x[-1])

print(S_posortowana)
