from race1 import Human
import random
from white_weapon import Dlugi_miecz

class Palladyn(Human):
    def __init__(self, name, age, sex, land):
        Human.__init__(self, name, age, sex, land)
        self.name = name
        self.age = age
        self.sex = sex
        self.land = land
        self.faith = 20
        self.white_weapons.append(Dlugi_miecz)

    def stats(self):
        print(
            f"Twoja siła wynosi: {self.power} punktów, wytrzymałość {self.strength}, masz {self.skill} punktów zręcznosci,"
            f"intelekt szacuję na {self.intelligence} punktów, ostrozność {self.caution} punktów. Charyzma to {self.charisma}"
            f"punktów, a życia pozostało Ci {self.health} punktów. Masz {self.faith} punktów specjalnych")

    def info(self):
        print(f"Szlachetny {self.name}, z dalekiej krainy {self.land}, na tym bezbożnym świecie już {self.age} rok")

    def deffence(self):
        print("Osłaniasz się damaceńską tarczą. Twojej obrony nie przełamie żadna siła, odzyskujesz oddech i wiarę"
              "w zwycięstwo")
        self.health += 5
        self.strength += 20
        self.faith += 5

    def recovery_special(self):
        print("Zakdłasza na szyję symbol mściwego Solkana, intonujesz wezwanie ostatniego kręgi. Twoje ciało przepełnia"
              "zimna moc, a rany się zablizniają")
        self.health += 15
        self.faith += 50

    def attack_with_wepon(self):
        if len(self.white_weapons) > 0:
            self.hit_points = self.white_weapon_points + self.power
            print(f"Atakujesz przeciwnika {Dlugi_miecz}, zadajesz {self.hit_points} punktów obrażeń")

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
        if self.faith >= 45:
            print("Długi runiczny miecz jarzy się niebieskim blaskiem. Oczy masz nieobecne, w Twoje ciało wstępuje Płomień."
                  "ze słowami: - Solkan est ira, Solkan mort est - ruszasz na wrogów")
            self.faith -= 65
            ira = (random.randint(1, 3))
            self.hit_points = self.power*ira +10
            if ira == 1:
                print(" Twoja wiara okazała się zbyt słaba, Solkan Cię nie wysłuchał")
            elif ira == 3:
                print("Gniew Solkana jest straszny. Tym razem objawia się w Twoim mieczu. Nieistotne, kto stanąl"
                      "naprzeciw Ciebie. Miał pecha")

        else:
            print("Nie jesteś godzien aby prosić o wsparcie Eru")

    def stilalive(self):
        if self.health >= 0:
            return True
        else:
            return False