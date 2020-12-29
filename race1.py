from abc import abstractmethod
import random

class Human():
    def __init__(self, name, age, sex, land):
        self.name = name
        self.age = age
        self.sex = sex
        self.land = land
        self.power = 100
        self.strength = 100
        self.skill = 100
        self.intelligence = 100
        self.caution = 100
        self.charisma = 100
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
            self.strength += random.randint(0, 10)
        elif x == 2:
            self.intelligence += random.randint(0, 10)
        elif x == 3:
            self.charisma += random.randint(0, 10)


    def attack(self):
        print("rozglądasz się za choćby kamieniem, jak na złosć nie ma nic. Trudno, gęba nie szklanka...")
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







