x = "myszykodujągdykotanieczują"

D = {}

for letter in x:

    if letter not in D.keys():
        D[letter] = 1

    else:
        D[letter] += 1

print(D)


S = {x:x+1 for x in range(10000) if x%23 == 0}

if 7430 in S:
    print(bool(True))

else:
    print(bool(False))

print(True if 7430 in S else False)


