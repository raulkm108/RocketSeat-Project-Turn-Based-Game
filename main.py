import random
from enemies_list import enemies

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
    
    def lvlup(self):
        self.__lvl = self.get_lvl()
        self.__lvl += 1
        print("You leveled up!")
        return self.__lvl
    
    
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
        return f"{super().show_details()}\nAbility: {self.get_ability()}\nType: {self.get_type()}"
    
class Game:
    def __init__(self) -> None:
        self.hero = Hero("Mage", 100, 5, "Fireball")

    def start_combat(self, enemy):
        print(f"\nStarting combat against {enemy.get_name()}!")
        while self.hero.get_hp() > 0 and enemy.get_hp() > 0:
            print("\nCurrent statuses: ")
            print(f"{self.hero.show_details()}\n{enemy.show_details()}")

            input("\nPress enter to choose your action... ")
            choice = input("1 - Attack, 2 - Ability: ")
            if choice == "1":
                self.hero.attack(enemy, self.hero.get_name())
            elif choice == "2":
                self.hero.use_ability(enemy, self.hero.get_name())
            else:
                print("Choose a valid option!\n")
            if enemy.get_hp() > 0:
                random_number = random.randint(1,2)
                if random_number == 1:
                    enemy.attack(self.hero, enemy.get_name())
                if random_number == 2:
                    enemy.use_ability(self.hero, enemy.get_name())
        
        if self.hero.get_hp() > 0:
            print("\nCongratulations, you won this combat!")
            self.hero.lvlup()
        else:
            print("\nYou have been defeated")

game = Game()
while True:
    random_enemy = random.choice(enemies)
    corrected_list = list(random_enemy.values())
    enemy = Enemy(*corrected_list)
    choice = input("Would you like to start a combat (1) or end programm (2)? ")
    if choice == "1":
        game.start_combat()
    elif choice == "2":
        break
    else:
        print("Choose a valid anwser")
