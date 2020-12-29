from race2 import Elf
import random
from magic_weapons import Zielony_plomien


class Elf_Mag(Elf):
    def __init__(self, name, age, sex, land):
        Elf.__init__(self, name, age, sex, land)
        self.name = name
        self.age = age
        self.sex = sex
        self.land = land
        self.meditation = 20
        self.magic_weapons.append(Zielony_plomien)


    def stats(self):
        print(
            f"Twoja siła wynosi: {self.power} punktów, wytrzymałość {self.strength}, masz {self.skill} punktów zręcznosci,"
            f"intelekt szacuję na {self.intelligence} punktów, ostrozność {self.caution} punktów. Charyzma to {self.charisma}"
            f"punktów, a życia pozostało Ci {self.health} punktów")

    def info(self):
        print(f"Z wysokieggo rodu elfów pochodzi {self.name}, urodzony w {self.land}, przeżył {self.age} lat")

    def deffence(self):
        print("Pierwsze krople spadają zdawałoby się na Twoje ciało, zamieniając się po chwili w rzęsity deszcz. W"
              "rzeczywystości woda opływa cię dosłownie o milimietr od ciała. Po chwili wodny płaszcz utwardza się,"
              "tworząc Aquaracenę - mocny, magiczny pancerz, który regeneruje Twoje siły witalne")
        self.health += 15
        self.strength += 17
        self.meditation += 10

    def recovery_special(self):
        print("Splatasz wiatry magii, przygotowując się do silnych zaklęć, regenerując zdrowie")
        self.health += 15
        self.meditation += 50

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
            print(f"{Zielony_plomien} jarzy się ostrym blaskiem, Twoich wrogów oplatają magiczne pnącza. "
                  f"Zadajesz {self.hit_points} punktów obrażeń")

        else:
            print("Nie posiadasz magicznej broni!")

    def special_attack(self):
        if self.meditation >= 200:
            print("Nie istnieje straszliwsze zaklęcie w  Elfów, niż Zupełne Wyzwolenie. Elf który go użyje musi"
                  "liczyć się z konsekwencjami, nawet gniewem Dhar za nadużywanie mocy. To będzie Twój problem, Twój wróg"
                  "ma większy. Nieszcześnik widzi wokól Ciebie tańczoncy wir ni to liści, ni to motyli o wściekle jaskrawych,"
                  "pastelowych kolorach, czuje mieszankę zniewalających, ziołowych zapachów, słyszy śpiew ptaków. Nie czuje"
                  "bólu, po chwili nic już nie czuje"
                  )
            self.meditation -= 200
            spirit = (random.randint(3, 6))
            self.hit_points = self.meditation * spirit + 10


            if spirit == 6:
                print("Gdy potęzna moc Elfa zostaje wsparta przez samego Dhar, nie nie ma nadziei dla żywych, lub umarłych"
                      "Ze znudzeniem obserwujesz jak ciała, i durne gęby wrpogów porasta błyskawicznie mech i trawa, by "
                      "po chwili stali się cześcią lasu.")


        else:
            print("Twoja moc nie jest wystarczająca na tak potężne zaklęcie")

    def stilalive(self):
        if self.health >= 0:
            return True
        else:
            return False