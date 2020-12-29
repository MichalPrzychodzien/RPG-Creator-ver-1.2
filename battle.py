import random
import time
from choose import choosen, choosen_next

print(
    "________________________________\n"
    "Wybór postaci. Dobrze zastanow się kogo wybrać: \n"
    "________________________________\n"
    "1 - Palladyn jest Świętnym Mścicielem, belitosnym rycerzen Solkana niszczącym każdy\n"
    "przejaw Chaosu. Walczy długim mieczem runicznym, jego atak specjalny zwieksza obrażenia fizyczne. Do ataku specjalnego\n"
    "potrzebujesz 50 pkt spec.\n"
    "________________________________\n"
    "2 - Ludzki Mag walczy magiczną bronią, używa potężnych zaklęć do pokonania wrogów. Atak specjalny i magiczny zalezy od\n"
    "inteligencji. Do ataku specjalnego potrzebujesz 50 pkt spec.\n"
    "________________________________\n"
    "3 - Krasnolud Artylerzysta walczy... altylerią! Przydatne są tu punkty zręczności. Do ataku specjalnego\n"
    "potrzebujesz 50 pkt spec.\n"
    "________________________________\n"
    "4 - Zabójca Troli to Krasnoludzki samobójca. Potężny młot bojowy i brutalna siła fizyczna, a także odwaga stanowią jego\n"
    "przewagi. Do ataku specjalnego potrzebujesz 50 pkt spec.\n"
    "________________________________\n"
    "5 - Leśny Duch jest niezwykłym Elfem. Używa długiego elfickiego łuku, ale dysponuje też sztyletem. Specjalny atak\n"
    "Leśnego Ducha nie zadaje obrażeń. Za to na jakiś czas używa kamuflarzu - staje się niewidzialny dla wroga. Do ataku\n"
    "specjalnego potrzebujesz 100 pkt spec.\n"
    "________________________________\n"
    "6 - Elf Mag to niemal istota z innego świata. Mało jest stworzeń zdolnych by z nim się mierzyć. Jego moc wyraża inteligencja,\n"
    "walczy magicznymi broniami. Atak specjalny kosztuje wiele punktów, lecz praktycznie kończy walkę. Do ataku specjalnego\n"
    "potrzebujesz 200 pkt spec.\n"
    "________________________________\n"
    "7 - Ork Bersaker to siła fizyczna i dziki szał. Tu brak inteligencji działa na korzyść. Do ataku specjalnego\n"
      "potrzebujesz 50 pkt spec.\n"
    "________________________________\n"
    "8 - Osk Szaman używa do zaklęć i walki magicznie spreparowanych szczątków, by wywołac demona i\n"
    "z jego pomocą sprowadzić burzę ognia. Do ataku specjalnego potrzebujesz 50 pkt spec.\n"
    "________________________________\n")




def starcie(player, player2):
    round = 1
    while player.stilalive() and player2.stilalive():
        print(f"Starcie {round} !")
        if random.randint(0, 1) == 0:
            print(f"walkę zaczyna {player.name}!")
            fight(player, player2)
        else:
            print(f"walkę zaczyna {player2.name}!")
            fight(player2, player)

        time.sleep(5)
        round += 1


def fight(x, y):
    x.stats()
    time.sleep(5)
    y.stats()
    time.sleep(5)
    if y.camuflage >= 1:
        y.camuflage -= 1
        print(f"{x.name} Nigdzie nie dostrzegasz przeciwnika!")
    else:
        print(f"{x.name} co chcesz zrobić? 1 - Atak bez broni, 2 - Obrona, 3 - Atak z bronią białą,\n"
              f"4 - Atak z bronią dystansową, 5 - Atak specjalny, 6 - Ozdyskanie specjala, 7 - Atak magiczny\n")
        f1 = int(input("Twój wybór: "))
        try:
            if f1 == 1:
                y.health -= (y.strength - x.attack())
                print(f"{x.name} zadał {y.name} {y.strength - x.hit_points} punktów obrażen")
            elif f1 == 2:
                x.deffence()

            elif f1 == 3:
                x.attack_with_wepon()

            elif f1 == 4:
                x.attack_with_range()

            elif f1 == 5:
                x.special_attack()

            elif f1 == 6:
                x.recovery_special()

            elif f1 == 7:
                x.magic_attack()
        except(ValueError, NameError):
            print("Przekroczyłeś zakres, lub nie podałaś cyfry. Żeby poprawnie wybrać, podaj cyfrę z zakresu 1 - 8 !!!")

    if x.camuflage >= 1:
        x.camuflage -= 1
        print(f"{y.name} Nigdzie nie dostrzegasz przeciwnika!")
    else:
        print(f"{y.name} co chcesz zrobić? 1 - Atak bez broni, 2 - Obrona, 3 - Atak z bronią białą,\n"
              f"4 - Atak z bronią dystansową, 5 - Atak specjalny, 6 - Ozdyskanie specjala, 7 - Atak magiczny\n")
        f2 = int(input("Twój wybór: "))
        try:
            if f2 == 1:
                x.health -= (x.strength - y.attack())
                print(f"{y.name} zadał {x.name} {x.strength - y.hit_points} punktów obrażen")

            elif f2 == 2:
                y.deffence()

            elif f2 == 3:
                y.attack_with_wepon()

            elif f2 == 4:
                y.attack_with_range()

            elif f2 == 5:
                y.special_attack()

            elif f2 == 6:
                y.recovery_special()

            elif f2 == 7:
                y.magic_attack()
        except(ValueError, NameError):
            print("Przekroczyłeś zakres, lub nie podałaś cyfry. Żeby poprawnie wybrać, podaj cyfrę z zakresu 1 - 8 !!!")


if __name__ == '__main__':
    starcie(choosen(), choosen_next())
