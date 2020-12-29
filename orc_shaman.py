from race4 import Orc
import random
from magic_weapons import Spreparowana_czaszka

class Shaman(Orc):
    def __init__(self, name, age, sex, land):
        Orc.__init__(self, name, age, sex, land)
        self.name = name
        self.age = age
        self.sex = sex
        self.land = land
        self.demon = 20
        self.magic_weapons.append(Spreparowana_czaszka)


    def stats(self):
        print(
            f"Twoja siła wynosi: {self.power} punktów, wytrzymałość {self.strength}, masz {self.skill} punktów zręcznosci,"
            f"intelekt szacuję na {self.intelligence} punktów, ostrozność {self.caution} punktów. Charyzma to {self.charisma}"
            f"punktów, a życia pozostało Ci {self.health} punktów")

    def info(self):
        print(f"Znany jako {self.name}, wyszedł z {self.land}, żyje w Hordzie {self.age} lat")

    def deffence(self):
        print("Demon Cię broni, i regeneruje")
        self.health += 10
        self.strength += 20
        self.demon += 10

    def recovery_special(self):
        print("wybijasz obłędny rytm na bębnie stworzonym z ludzkiej skóry. Wchodzisz w trans ")
        self.health += 20
        self.demon += 50

    def attack_with_wepon(self):
        if len(self.white_weapons) > 0:
            self.hit_points = self.white_weapon_points + self.power
            print(f"Atakujesz przeciwnika, zadajesz {self.hit_points} punktów obrażeń")

        else:
            print("Nie posiadasz białej broni!")

    def magic_attack(self):
        if len(self.magic_weapons) > 0:
            self.hit_points = self.magic_points + self.intelligence
            print(f"Tańczysz w szaleńczym rytmie, ognisty podmuch uderza we wrogów. "
                  f"Zadajesz {self.hit_points} punktów obrażeń")

        else:
            print("Nie posiadasz magicznej broni!")

    def attack_with_range(self):
        if len(self.range_weapons) > 0:
            self.hit_points = self.range_points + self.skill
            print(f"Zadajesz {self.hit_points} obrażeń")

        else:
            print("Nie posiadasz broni dystansowej")

    def special_attack(self):
        if self.demon >= 50:
            print(f"{Spreparowana_czaszka} stała się bramą demona, potwetrze pachnie dymem i siarką")
            self.demon -= 50
            fire = random.randint(1, 3)
            if fire == 1:
                print(f"Dziwne słowa mowy Chaosu wypływają z ludzkiej {Spreparowana_czaszka}. Burza ognia spływająca z nieba"
                      f"przypomina najgorszy koszmar")
            elif fire == 3:
                print("Demony Chaosu są nieprzewidywalne. Ten nie okazał Ci wsparcia, zamiast ognistego uderzenia"
                      "spada zwykły magiczny podmuch")

            self.hit_points = self.intelligence*fire
            print(f"Zadajesz {self.hit_points} obrażeń")


        else:
            print("Nie dość głęboko wszedłeś w trans")

    def stilalive(self):
        if self.health >= 0:
            return True
        else:
            return False