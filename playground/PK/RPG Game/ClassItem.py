class Item:
    def __init__(self, name, value, drop_chance):
        self.name = name
        self.value = value
        self.drop_chance = drop_chance

    def add_iteam(self, target):
        target.backpack.append(self)

    def is_in_equipment(self, equipment):
        if self in equipment:
            return True
        
    def __repr__(self):
        return self.name

class Potion(Item):
    def __init__(self, name, value, drop_chance, toxicity, health_addion, mana_addion):
        super().__init__(name, value, drop_chance)
        self.toxicity = toxicity
        self.health_addion = health_addion
        self.mana_addion = mana_addion

    # def health_add(self, health_points, toxicity, player):
    #     health_points += self.health_addion
    #     self.toxicity_add(toxicity, player)
    
    # def mana_add(self, mana_points, toxicity, player):
    #     mana_points += self.mana_addion
    #     self.toxicity_add(toxicity, player)

    # def toxicity_add(self, toxicity, player):
    #     toxicity += self.toxicity
    #     # self.potion_used(player)

    def potion_used(self,player):
        player.backpack.remove(self)
        print('Potion used')


class Armor(Item):
    def __init__(self, name, value, drop_chance, defence_addion):
        super().__init__(self, name, value, drop_chance)
        self.defence_addion = defence_addion

    def defence_add(self, defence_points):
        defence_points += self.defence_addion


class Weapon(Item):
    def __init__(self, name, value, drop_chance, damage_addion):
        super().__init__(self, name, value, drop_chance)
        self.damage_addion = damage_addion

    def damage_add(self, damage):
        damage += self.damage_addion 
