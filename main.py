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
        return f"Name: {self.get_name()}\nHp: {self.get_hp()}\nLvl: {self.get_lvl()}"
    
class Hero(Character):
    def __init__(self, name, hp, lvl, ability):
        super().__init__(name, hp, lvl)
        self.__ability = ability
    
    def get_ability(self):
        return self.__ability
    
    def show_details(self):
        return f"{super().show_details()}\nAbility: {self.get_ability()}\n"
    
class Enemy(Character):
    def __init__(self, name, hp, lvl, type):
        super().__init__(name, hp, lvl)
        self.__type = type

    def get_type(self):
        return self.__type
    
    def show_details(self):
        return f"{super().show_details()}\nType: {self.get_type()}"
    
class Game:
    def __init__(self) -> None:
        self.hero = Hero("Mage", 100, 5, "Fireball")
        self.enemy = Enemy("Crab", 30, 2, "Water")

    def start_combat(self):
        print("\nStarting combat!")
        while self.hero.get_hp() > 0 and self.enemy.get_hp() > 0:
            print("\nCurrent statuses: ")
            print(f"{self.hero.show_details()}\n{self.enemy.show_details()}")

            input("\nPress enter to choose your action... ")
            choice = input("1 - Attack, 2 - Ability: ")

game = Game()
game.start_combat()
