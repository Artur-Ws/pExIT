
def zwracaj_kolejne_parzyste():
    for n in range(2, 20, 2):
        yield n


z = zwracaj_kolejne_parzyste()

# for i in range (10):
#     print(next(z))

y = ('a' * n for n in range(5))

for i in range(5):
    print(next(y))


def x():
    for n in range(5,55,5):
        yield n

z = x()

for i in range(10):
    print(next(z))