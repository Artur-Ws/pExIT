A = [1,2,3,3,2,1,2,3]

B = []

# 1. Rozw. pierwsze -> iteracja przez elementy listy A i sprawdzenie czy się powtarzają
for i in A:
    if i in B:
        break
    else:
        B.append(i)

print(B)

# 2. Rozw. drugie -> zamiana listy na set

C = list(set(A))

print(C)