class Character:
    def __init__(self, name, healt_points, strenght):
        self.name = name
        self.health_points = healt_points
        self.strenght = strenght
    
    def get_damage(self, damage):
        self.health_points = self.health_points - damage

#inicialisation
player = Character("Player", 100, 20)
enemy1 = Character("Orc", 80, 25)
enemy2 = Character("Goblin", 20, 8)
print(player.name, player.health_points, player.strenght)
print(enemy2.health_points)
player.get_damage(30)
print(player.health_points)