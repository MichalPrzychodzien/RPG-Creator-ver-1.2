from race4 import Orc
import random
from white_weapon import Topor


class Bersaker(Orc):
    def __init__(self, name, age, sex, land):
        Orc.__init__(self, name, age, sex, land)
        self.name = name
        self.age = age
        self.sex = sex
        self.land = land
        self.madnes = 20
        self.white_weapons.append(Topor)

    def stats(self):
        print(
            f"Twoja siła wynosi: {self.power} punktów, wytrzymałość {self.strength}, masz {self.skill} punktów zręcznosci,"
            f"intelekt szacuję na {self.intelligence} punktów, ostrozność {self.caution} punktów. Charyzma to {self.charisma}"
            f"punktów, a życia pozostało Ci {self.health} punktów")

    def info(self):
        print(f" Waleczny {self.name}, prawdopodobnie pochodzący z {self.land}, udało mu się przeżyć {self.age} lat")

    def deffence(self):
        print("Obrona to największa bzdura, kto tak robi? Krzyrzujesz swoje potężna łapy, przyklękasz na kolano, "
              "i pomijasz atak. Odzyskujesz trochę sił.")
        self.health += 10
        self.strength += 20
        self.madnes += 10

    def recovery_special(self):
        print("Słyszysz zielona pieśń, las słyszy Ciebie, i uzdrawia. ")
        self.health += 20
        self.madnes += 50

    def attack_with_wepon(self):
        if len(self.white_weapons) > 0:
            self.hit_points = self.white_weapon_points + self.power
            print(f"Atakujesz przeciwnika {Topor}, zadajesz {self.hit_points} punktów obrażeń")

        else:
            print("Nie posiadasz białej broni!")

    def attack_with_range(self):
        if len(self.range_weapons) > 0:
            self.hit_points = self.range_points + self.skill
            print(f"Zadajesz {self.hit_points} obrażeń")

        else:
            print("Nie posiadasz broni dystansowej")

    def magic_attack(self):
        if len(self.magic_weapons) > 0:
            self.hit_points = self.magic_points + self.intelligence
            print(f"Zadajesz {self.hit_points} punktów obrażeń")

        else:
            print("Nie posiadasz magicznej broni!")

    def special_attack(self):
        if self.madnes >= 50:
            print("Twoje oczy zachodzą czerwoną mgłą. Czas zwalnia. Wrogowie poruszają się jak muchy w smole, są słabi jak"
                  "dzieci. W morderczym szale ruszasz do ataku. ")
            self.madnes -= 50
            charge = random.randint(1, 3)
            if charge == 1:
                print("Rozpędzony potykasz się o głowę jakiegoś nieszczęsnika, i wpadasz w końskie truchło pełne żygowin,"
                      "krwi i gówna. Jakby tego było mało Twój topur ląduje centymetry od Twojej głowy")
            elif charge == 3:
                print("Twój ociekający krwią topór miażdży tarcze, gruchocze czaszki, rozrywa ciała. To istna rzeź")

            self.hit_points = self.power*charge


        else:
            print("Nie posmakowałeś jeszcze dość krwi, mordercza żądza nie wzbiera")

    def stilalive(self):
        if self.health >= 0:
            return True
        else:
            return False