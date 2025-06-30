class Character:
    def __init__(self, name, hp, lvl):
        self.__name = name
        self.__hp = hp
        self.__lvl = lvl

    def get_name(self):
        return self.__name
    
    def get_hp(self):
        return self.__hp
    
    def get_lvl(self):
        return self.__lvl
    
    def show_details(self):
        return f"Name: {self.get_name()}\nHp: {self.get_hp()}\nLvl: {self.get_lvl()}\n"
    
class Hero(Character):
    def __init__(self, name, hp, lvl, ability):
        super().__init__(name, hp, lvl)
        self.__ability = ability
    
    def get_ability(self):
        return self.__ability
    
class Enemy(Character):
    def __init__(self, name, hp, lvl, type):
        super().__init__(name, hp, lvl)
        self.__type = type

    def get_type(self):
        return self.__type
    
    
hero = Hero("Mage", 100, 5, "Fireball")
print(hero.show_details())

enemy = Enemy("Crab", 30, 2, "Water")
print(enemy.show_details())