from abc import abstractmethod
import random

class Orc():
    def __init__(self, name, age, sex, land):
        self.name = name
        self.age = age
        self.sex = sex
        self.land = land
        self.power = 135
        self.strength = 120
        self.skill = 75
        self.intelligence = 80
        self.caution = 80
        self.charisma = 65
        self.health = 1200
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
            self.power += random.randint(0, 10)
        elif x == 2:
            self.strength += random.randint(0, 10)
        else:
            self.charisma += random.randint(0, 10)



    def attack(self):
        print("Nie masz czym walczyć. Przecież nigdy nie było to przeszkodą. Oblizując kły, warczysz: zabić! - i ruszasz do walki")
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