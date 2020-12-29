from race3 import Dwarf
import random

class Dwarf_Gunner(Dwarf):
    def __init__(self, name, age, sex, land):
        Dwarf.__init__(self, name, age, sex, land)
        self.name = name
        self.age = age
        self.sex = sex
        self.land = land
        self.prepare = 20

    def stats(self):
        print(
            f"Twoja siła wynosi: {self.power} punktów, wytrzymałość {self.strength}, masz {self.skill} punktów zręcznosci,"
            f"intelekt szacuję na {self.intelligence} punktów, ostrozność {self.caution} punktów. Charyzma to {self.charisma}"
            f"punktów, a życia pozostało Ci {self.health} punktów")

    def info(self):
        print(f"{self.name}, weteran niejednej bitwy pochodzący z {self.land}, liczy sobie {self.age} lat")

    def deffence(self):
        print("Skrywasz się za masywną bronią, która sprawdza się jako niezła osłona")
        self.health += 10
        self.strength += 20
        self.prepare += 10

    def recovery_special(self):
        print("Krzątasz się wokół altylerii, przygotowując ją do strzału. ")
        self.health += 20
        self.prepare += 50

    def attack_with_wepon(self):
        if len(self.white_weapons) > 0:
            self.hit_points = self.white_weapon_points + self.power
            print(f"Atakujesz przeciwnika, zadajesz {self.hit_points} punktów obrażeń")

        else:
            print("Nie posiadasz białej broni!")

    def attack_with_range(self):
        if len(self.range_weapons) > 0:
            self.hit_points = self.range_points + self.skill
            print(f"po raz kolejny działo przemówiło! Zadajesz {self.hit_points} obrażeń")

        else:
            print("Nie posiadasz broni dystansowej")

    def magic_attack(self):
        if len(self.magic_weapons) > 0:
            self.hit_points = self.magic_points + self.intelligence
            print(f"Zadajesz {self.hit_points} punktów obrażeń")

        else:
            print("Nie posiadasz magicznej broni!")

    def special_attack(self):
        if self.prepare >= 50:
            print("Twoi wrogowie z pewnością zachodzą w głowę, czym jest ta dziwna żeliwna rura ozdobiona runami, wokół"
                  "której się uwijasz. Nie każesz im dłużej czekać, w obłoku gęstego, gryzącego dymu krasnoludzka armata"
                  "wypluwa ciężki kartacz")
            self.prepare -= 50
            shot = random.randint(1, 2)
            if shot == 1:
                print("Co za spektakularny niewypał! Kartacz eksplodował niemal pod Twoim nosem, osmalając Twoją bujną brodę,"
                      "wrogowie z miejsca mogliby Cię posiekać, gdyby nie to że pokładają się ze śmiechu.")
            elif shot == 2:
                print("Kartacz wpada pomiędzy szeregi Twoich wrogów, odłami po eksplozji przebijają pancerze,"
                      "tną ciałą i powodują poważne obrażenia")

        else:
            print("Altyleria nie jest gotowa, musisz się lepiej przygotować")

    def stilalive(self):
        if self.health >= 0:
            return True
        else:
            return False