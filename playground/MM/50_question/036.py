class Pies:

    def __init__(self, imie, rasa):
        self.imie = imie
        self.rasa = rasa

    def __str__(self):
        return f"Pies rasy {self.rasa} ma na imie {self.imie}"


maly_pies = Pies("Pikuś", "ratlerek")

print(maly_pies)
print(maly_pies.imie, maly_pies.rasa)


class Kot:

    def __init__(self, imie, kolor):
        self.imie = imie
        self.kolor = kolor

    def __str__(self):
        return f"Kot {self.imie} jest {self.kolor}"


k = Kot("Mruczek", "rudy")

print(k)
