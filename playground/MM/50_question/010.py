m = {'m': 1, 'y': 3, 's': 1, 'z': 2, 'k': 2, 'o': 3, 'd': 2, 'u': 2, 'j': 2, 'ą': 2, 'g': 1, 't': 1, 'a': 1, 'n': 1, 'i': 1, 'e': 1, 'c': 1}
l = []

for letter in m.keys():

    if m[letter] == 4:
        l.append(True)
    else:
        l.append(False)

if True in l:
    print(True)

else:
    print(False)

print(list(m.values()))

if 4 in m.values():
    print(True)

else:
    print(False)

print(True if 4 in m.values() else False)

pensje = {'ksiegowa': 5000, 'kierowca': 4500, 'recepcjonistka': 4000}

print(sum(pensje.values()))
