class Matematyka:

    def __init__(self):
        self.pi = 3.14

    def policz_obwod_okregu(self,r):
        return 2 * self.pi * r

    @staticmethod
    def dodaj(a, b):

        return a + b

    # @staticmethod
    # def dodaj_i_pomnoz(a, b):
    #     return dodaj(a, b) * 2

    @classmethod
    def dodaj_i_pomnoz(cls, a, b):
        return cls.dodaj(a, b) * 2


m = Matematyka()
print(m.policz_obwod_okregu(5))
print(Matematyka.dodaj(5, 902))
print(Matematyka.dodaj_i_pomnoz(5, 902))
