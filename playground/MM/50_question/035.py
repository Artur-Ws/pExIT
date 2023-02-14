class Pies:

    def __init__(self, imie, rasa):
        self.imie = imie
        self.rasa = rasa


maly_pies = Pies("Pikuś", "ratlerek")
duzy_pies = Pies("Killer", "doberman")

print(maly_pies.imie, maly_pies.rasa)
print(duzy_pies.imie, duzy_pies.rasa)


class Kot:

    def __init__(self, imie, kolor):
        self.imie = imie
        self.rasa = kolor


k = Kot("Mruczek", "czarny")

print(k.imie, k.kolor)

