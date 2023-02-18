from random import randint

A = [randint(0,100) for i in range(5)]
B = [randint(0,100) for i in range(5)]
H = [randint(0,100) for i in range(5)]

max_v = 0

print(A)
print(B)
print(H)

for a in A:
    for b in B:
        for h in H:
            V = a * b * h
            if V > max_v:
                max_v = V

print(max_v)

max_v = max(A) * max(B) * max(H)

print(max_v)
