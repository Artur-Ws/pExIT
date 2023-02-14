n = input("Jaki zakres wariacie? n = ")


FizzBuzz = []

for i in range(1, int(n) + 1):

    if i % 15 == 0:
        FizzBuzz.append("FizzBuzz")

    elif i % 3 == 0:
        FizzBuzz.append("Fizz")

    elif i % 5 == 0:
        FizzBuzz.append("Buzz")

    else:
        FizzBuzz.append(i)

for i in FizzBuzz:
    print(i)

print()
print("*------------------*")
print()


def fizzbuzz_1(numbero):

    for num in range(1, numbero + 1):
        if num % 15 == 0:
            print("FizzBuzz")

        elif num % 3 == 0:
            print("Fizz")

        elif num % 5 == 0:
            print("Buzz")

        else:
            print(str(num))


fizzbuzz_1(45)

print()
print("*------------------*")
print()

def fizzbuzz_2(numba):

    for i in range(1, numba + 1):
        wynik = ''

        if i % 3 == 0:
            wynik += "Fizz"

        if i % 5 == 0:
            wynik += "Buzz"

        if i % 3 != 0 and i % 5 != 0:
            wynik = str(i)

        print(wynik)


fizzbuzz_2(45)
