from abc import abstractmethod
import random

class Dwarf():
    def __init__(self, name, age, sex, land):
        self.name = name
        self.age = age
        self.sex = sex
        self.land = land
        self.power = 117
        self.strength = 130
        self.skill = 70
        self.intelligence = 85
        self.caution = 70
        self.charisma = 82
        self.health = 1100
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

        x = int(input("który element chcesz podrasować: 1. Siła, 2. Wytrzymałość, 3. Charyzma: "))
        if x == 1:
            self.strength += random.randint(0, 10)
        elif x == 2:
            self.caution += random.randint(0, 10)
        else:
            self.charisma += random.randint(0, 10)



    def attack(self):
        print("Twoje potęzne pięści zawsze były najlepszą bronią. Z odwietrznym zawołaniem: Na chwałę przodków! - ruszasz na wroga")
        self.hit_points = self.power + (random.randint(0, 10))
        return self.hit_points

    @abstractmethod
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