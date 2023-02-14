class ZwierzeLadowe:

    def przedstaw_sie(self):
        print("Jestem zwierzęciem lądowym.")

    def biegaj(self):
        print("Biegam tu i tam.")


class ZwierzeMorskie:

    def przedstaw_sie(self):
        print("Jestem zwierzęciem morskim.")

    def plywaj(self):
        print("Pływam tu i tam.")


class SwinkaMorska(ZwierzeLadowe, ZwierzeMorskie):
    pass


swinka = SwinkaMorska()
swinka.przedstaw_sie()
swinka.biegaj()
swinka.plywaj()

