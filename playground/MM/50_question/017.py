A = [4, 5, 7, -3, 2, 8, -10, 15]

print(min(A))
print(max(A))
print(max(A) - min(A))

mini = A[0]
maxi = A[0]

for i in A:
    if i < mini:
        mini = i
    elif i > maxi:
        maxi = i

print(maxi - mini)

A = [x**2 + 3 for x in range(10)]

print(A)

print(True if max(A) > 99 else False)