def dodaj_gwiazdki(funkcja):

    def funkcja_udekorowana():

        print("***")
        funkcja()
        print("***")

    return funkcja_udekorowana

@dodaj_gwiazdki
def f():
    print("Cześć, jestem f()")

f()

