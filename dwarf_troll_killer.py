from race3 import Dwarf
import random
from white_weapon import Mlot_bojowy

class Dwarf_Troll_Killer(Dwarf):
    def __init__(self, name, age, sex, land):
        Dwarf.__init__(self, name, age, sex, land)
        self.name = name
        self.age = age
        self.sex = sex
        self.land = land
        self.madnes = 20

    def stats(self):
        print(
            f"Twoja siła wynosi: {self.power} punktów, wytrzymałość {self.strength}, masz {self.skill} punktów zręcznosci,"
            f"intelekt szacuję na {self.intelligence} punktów, ostrozność {self.caution} punktów. Charyzma to {self.charisma}"
            f"punktów, a życia pozostało Ci {self.health} punktów")

    def info(self):
        print(f"{self.name} - stary krasnoludzki wiarus, urodzony w {self.land}, żyje juz {self.age} lat i wciąż nie może zginąć")

    def deffence(self):
        print(" - Co? Ja? Obrona? - drapiesz się po łysym wytatułowanym łbie. Sam nie wiesz o co Ci chodzi, ale osłaniasz"
              "się ogromnym młotem bojowym")
        self.health += 5
        self.strength += 20
        self.madnes += 10

    def recovery_special(self):
        print("Powracają wspomnieina. Krzyk, płacz kobiet i dzieci z Twojej osady, wyrzynanych przez najeźdców. Sceny widziane"
              "jak przez mgłę, gdy pijany nie potrafiłeś podnieść broni. Hańba, hańba, wstyd i gniew.. ")
        self.health += 15
        self.madnes += 60

    def attack_with_wepon(self):
        if len(self.white_weapons) >= 0:
            self.hit_points = self.white_weapon_points + self.power
            print(f"Atakujesz przeciwnika {Mlot_bojowy}, zadajesz {self.hit_points} punktów obrażeń")

        else:
            print("Nie posiadasz białej broni!")

    def attack_with_range(self):
        if len(self.range_weapons) >= 1:
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
            print("Samobójcza śmierć w chwalebnej walce to jedyny sposób byćś mył swoją hańbę. Na zgóbę Twoich wrogów,"
                  "w morderczym szale ruszasz do ataku")
            self.madnes -= 50
            red = random.randint(1, 3)
            if red == 1:
                print("Znowu wychodzi Twoja słaba, tchurzliwa natura. Pomimo rozpoczętej szarży dopadają Cię wątpliwośc,"
                      " zwalniasz, osłaniasz się, walczysz ostrożnie. Tzn, jak na zabójcę troli.")
            elif red == 2:
                print("Niewiele pamiętasz z tego co się dzieje, wiesz tylko że 50kg młot bojowy jest lekki jak piórko."
                      "Obuch roztrzaskuje czaszki niczym dojrzałe arbuzy, po chwili nie ma już co zbierać."
                      "To nie jest dobry dzień, znów nie udało Ci się zginąć")

            self.hit_points = self.power*red


        else:
            print("Czujesz nie dość mocno swą hańbę, aby rzucić się do samobójczego ataku")

    def stilalive(self):
        if self.health >= 0:
            return True
        else:
            return False