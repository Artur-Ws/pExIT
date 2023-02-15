pierwsza_szuflada = ['majtki', 'skarpetki', 'koszulki']
druga_szuflada = ['notes', 'spinacze', 'ołówek']
trzecia_szuflada = ['puzzle', 'gry PC', 'album ze zdjęciami']

szafka = [pierwsza_szuflada, druga_szuflada, trzecia_szuflada]

druga_szuflada.append('długopis')
print(szafka)

for szuflada in szafka:
    print(szuflada)

A = [[1, 2], [3, 4]]
A[1][0] = 'trzy'

print(A)