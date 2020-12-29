from abc import abstractmethod
import random

class Elf():
    def __init__(self, name, age, sex, land):
        self.name = name
        self.age = age
        self.sex = sex
        self.land = land
        self.power = 95
        self.strength = 75
        self.skill = 125
        self.intelligence = 115
        self.caution = 120
        self.charisma = 110
        self.health = 1000
        self.white_weapons = []
        self.magic_weapons = []
        self.range_weapons = []
        self.armour = []
        self.hit_points = 0
        self.range_points = 0
        self.magic_points = 0
        self.white_weapon_points = 0
        self.armour_point = 0
        self.camuflage = 0

        x = int(input("który element chcesz podrasować: 1. Zręczność, 2. Intelekt, 3. Ostrozność: "))
        if x == 1:
            self.skill += random.randint(0, 10)
        elif x == 2:
            self.intelligence += random.randint(0, 10)
        else:
            self.caution += random.randint(0, 10)

    @abstractmethod
    def attack(self):
        print("Są sytuacje że nawety ty musisz podjąc walkę bez broni. Wzywając z myślach Eldarów, przygotowujesz się do starcia")
        self.hit_points = self.power + (random.randint(0, 10))
        return self.hit_points

    def deffence(self):
        print("Osłaniasz się jak umiesz")
        self.health += 5
        self.strength += 10

    @abstractmethod
    def stilalive(self):
        if self.health >= 0:
            return True
        else:
            print("jesteś trupem!")
            return False