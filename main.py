import random

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
    
    def take_damage(self, damage):
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0
        return

    def attack(self, target, attacker):
        randomizer = round(random.uniform(1,3), 2)
        damage = int(self.__lvl * randomizer)
        print(f"\nThe {attacker} rolled {randomizer} between 1 and 3")
        print(f"{self.get_name()} attacked {target.get_name()} and did {damage} damage!")
        #possible otimization: turn the next block in a diferent function caleed "take_damage"
        target.take_damage(damage)

    def use_ability(self, target, attacker):
        randomizer = round(random.uniform(2,4), 2)
        damage = int(self.get_lvl() * randomizer)
        target.take_damage(damage)
        print(f"\nThe {attacker} rolled {randomizer} between 2 and 4")
        print(f"{self.get_name()} used {self.get_ability()} on {target.get_name()} and did {damage} damage!")
    
class Hero(Character):
    def __init__(self, name, hp, lvl, ability):
        super().__init__(name, hp, lvl)
        self.__ability = ability
    
    def get_ability(self):
        return self.__ability
    
    def show_details(self):
        return f"{super().show_details()}\nAbility: {self.get_ability()}\n"
    
    
class Enemy(Character):
    def __init__(self, name, hp, lvl, ability, type):
        super().__init__(name, hp, lvl)
        self.__type = type
        self.__ability = ability

    def get_ability(self):
        return self.__ability

    def get_type(self):
        return self.__type
    
    def show_details(self):
        return f"{super().show_details()}\nType: {self.get_type()}"
    
class Game:
    def __init__(self) -> None:
        self.hero = Hero("Mage", 100, 5, "Fireball")
        self.enemy = Enemy("Crab", 30, 3,"Claw Burst", "Water")

    def start_combat(self):
        print("\nStarting combat!")
        while self.hero.get_hp() > 0 and self.enemy.get_hp() > 0:
            print("\nCurrent statuses: ")
            print(f"{self.hero.show_details()}\n{self.enemy.show_details()}")

            input("\nPress enter to choose your action... ")
            choice = input("1 - Attack, 2 - Ability: ")
            if choice == "1":
                self.hero.attack(self.enemy, self.hero.get_name())
            elif choice == "2":
                self.hero.use_ability(self.enemy, self.hero.get_name())
            else:
                print("Choose a valid option!\n")
            if self.enemy.get_hp() > 0:
                random = random.randint(1,2)
                if random == 1:
                    self.enemy.attack(self.hero, self.enemy.get_name())
                if random == 2:
                    self.enemy.use_ability(self.hero, self.enemy.get_name())
        
        if self.hero.get_hp() > 0:
            print("\nCongratulations, you won this combat!")
        else:
            print("\nYou have been defeated")

game = Game()
game.start_combat()
