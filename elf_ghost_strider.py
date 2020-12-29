from race2 import Elf
import random
from white_weapon import Sztylet
from range_weapon import Dlugi_luk_elfow

class Ghost_Strider(Elf):
    def __init__(self, name, age, sex, land):
        Elf.__init__(self, name, age, sex, land)
        self.name = name
        self.age = age
        self.sex = sex
        self.land = land
        self.forest_spirit = 20
        self.range_weapons.append(Dlugi_luk_elfow)
        self.white_weapons.append(Sztylet)

    def stats(self):
        print(
            f"Twoja siła wynosi: {self.power} punktów, wytrzymałość {self.strength}, masz {self.skill} punktów zręcznosci,"
            f"intelekt szacuję na {self.intelligence} punktów, ostrozność {self.caution} punktów. Charyzma to {self.charisma}"
            f"punktów, a życia pozostało Ci {self.health} punktów")

    def info(self):
        print(f"Zwą Cię {self.name}, z nieznanego {self.land}, liczysz sobie {self.age} lat")

    def deffence(self):
        print("Gałąż, kamień, konar stanowią Twoją osłonę. Wzmacniasz się, i odzyskujesz zdrowie")
        self.health += 10
        self.strength += 20
        self.forest_spirit += 10

    def recovery_special(self):
        print("Słyszysz zielona pieśń, las słyszy Ciebie, i uzdrawia.")
        self.health += 20
        self.forest_spirit += 50

    def attack_with_wepon(self):
        if len(self.white_weapons) > 0:
            self.hit_points = self.white_weapon_points + self.power
            print(f"Atakujesz przeciwnika za pomocą {Sztylet}, zadajesz {self.hit_points} punktów obrażeń")

        else:
            print("Nie posiadasz białej broni!")

    def attack_with_range(self):
        if len(self.range_weapons) > 1:
            self.hit_points = self.range_points + self.skill
            print(f"Twój łuk wypuszcza kolejną śmiercionośną strzałę. Zadajesz {self.hit_points} obrażeń")

        else:
            print("Nie posiadasz broni dystansowej")

    def magic_attack(self):
        if len(self.magic_weapons) > 0:
            self.hit_points = self.magic_points + self.intelligence
            print(f"Zadajesz {self.hit_points} punktów obrażeń")

        else:
            print("Nie posiadasz magicznej broni!")

    def special_attack(self):
        if self.forest_spirit >= 100:
            print(f"Twoje ciało jest trawą, drzewem, mchem i strumieniem. Twój głos jest śpiewem ptaków, szum wiatru "
                  "maskuje Twoje ruchy. Tylko świst zatrutych strzał nie da się pomylić z niczym. Jesteś niewidzialny "
                  f"przez {self.camuflage} rund")
            self.forest_spirit -= 100
            camuflage = (random.randint(1, 3))
            self.camuflage = camuflage


        else:
            print("Nie zjednoszyłeś się z lasem, Twoj wróg ciągle Cię widzi")

    def stilalive(self):
        if self.health >= 0:
            return True
        else:
            return False