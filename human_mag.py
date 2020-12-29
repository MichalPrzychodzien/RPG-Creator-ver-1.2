from race1 import Human
import random
from magic_weapons import Kostur_z_onyksem


class Mag(Human):
    def __init__(self, name, age, sex, land):
        Human.__init__(self, name, age, sex, land)
        self.name = name
        self.age = age
        self.sex = sex
        self.land = land
        self.meditation = 30
        self.magic_weapons.append(Kostur_z_onyksem)


    def stats(self):
        print(
            f"Twoja siła wynosi: {self.power} punktów, wytrzymałość {self.strength}, masz {self.skill} punktów zręcznosci,"
            f"intelekt szacuję na {self.intelligence} punktów, ostrozność {self.caution} punktów. Charyzma to {self.charisma}"
            f"punktów, a życia pozostało Ci {self.health} punktów")

    def info(self):
        print(f"Uczony {self.name}, pochodzący z {self.land}, życje {self.age} lat")

    def deffence(self):
        print("Skupiasz swoją moc tworząc mentalny pancerz wokół ciała. Regenreujesz zdrowie i siły duchowe")
        self.health += 5
        self.strength += 20
        self.meditation += 10

    def recovery_special(self):
        print("Myśli kierujesz w stronę znaków tworzących Wszechrzecz. Kodeks wypełnia Twój umysł")
        self.health += 10
        self.meditation += 40

    def attack_with_wepon(self):
        if len(self.white_weapons) > 0:
            self.hit_points = self.white_weapon_points + self.power
            print(f"Atakujesz przeciwnika, zadajesz {self.hit_points} punktów obrażeń")

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
            print(f"Kreślisz runę ataku, zadajesz {self.hit_points} punktów obrażeń")

        else:
            print("Nie posiadasz magicznej broni!")


    def special_attack(self):
        if self.meditation >= 50:
            print(
                "Wznosisz swój kostór zakończony oprawionym onyksem. Powietrze staje się cięzkie, zrywa się wicher. "
                "Niebo przesłaniają fioletowe chmury, powietrze pachnie ozonem.")
            self.meditation -= 50
            med = (random.randint(1, 2))
            self.hit_points = self.intelligence*med + 20
            if med == 1:
                print("Wiatr cichnie, chumury znikają. Kodeks nie sprzyja słabym")
            elif med == 2:
                print("Świat jest napisany Znakami Kodeksu. Ty zmieniasz rzeczywistośc, jedną myslą. Czarne pioruny magii"
                      "obracają w pył Twoich wrogów")

        else:
            print("Naprawdę jesteś Magiem? W tej chwili nie dysponujesz mocą")

    def stilalive(self):
        if self.health >= 0:
            return True
        else:
            return False