from dwarf_gunner import Dwarf_Gunner
from orc_shaman import Shaman
from orc_bersaker import Bersaker
from elf_mag import Elf_Mag
from elf_ghost_strider import Ghost_Strider
from human_palladyn import Palladyn
from human_mag import Mag
from dwarf_troll_killer import Dwarf_Troll_Killer

def choosen():
    try:
        global player

        x = int(input("---------------------\n"
        "Pierwszy gracz, kogo wybierasz?:\n "
        "1 - Palladyn, 2 - ludzki Mag, 3 - Krasnoludzki Atylerzysta,\n"
        "4 - Zabojca Troli, 5 - Leśny Duch, 6 - Elf Mag, 7 - Ork Bersaker, 8 - Szaman Orków: \n "))
        if x == 1:
            print("Jesteś Palladynem, szlachetnym wojownikiem walczącym ze złem. Nie lękasz się nikogo, nie istnieje wróg\n"
              "zdolny pokonć Wszechmocnego Eru")
            player = Palladyn(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "), input("skąd pochodzisz: "))

        elif x == 2:
            print("Ukończyłeś z wyróżnieinem magdeburskie kolegium Magii Kodeksu. Ludzie traktuję cię z nieufnością i strachem,\n "
                  "co nie przeszkada im oferować imperialne dukaty za Twoje usługi.")
            player = Mag(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "), input("skąd pochodzisz: "))


        elif x == 3:
            print("Spośród masy krasnoludów - wariatów artylerzyści z pewnością są ciekawą grupą. Brak palców, poparzona paskudna\n"
                  "gęba, całkowita lubb częsciowa głuchota. Sprzęt przy którym pracują najczęściej jest bardzo zawodny\n."
                  "Mimo tych mankamentów jesteś cenionym i poszukiwanym nabytkiem do każdej armii, oddziału najmeników\n"
                  "a także kopalni czy zespołu inzynierów\n")
            player = Dwarf_Gunner(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "), input("skąd pochodzisz: "))

        elif x == 4:
            print("Nie ma gorszej dla krasnoluda rzeczy pod słońcem jak okryć się hańbą. Hańba imienia, pamięci, rodu. Niszczy ona\n"
                  "i zatruwa sumienie takiego krasnoluda, a wbrew całemu krasnoludzkiemu chamstwu i grubianstwu, mają oni przecież\n"
                  "poczucie sprawiedliwości, i mocny kręgosłup moralny. Jeśli więc wybierasz tą drogę, nieszczęśniku, masz tylko jeden\n"
                  "cel. Zmazać Twoje zbrodnie piękną, chwalebną śmiercią w samobójczej walce\n")
            player = Dwarf_Troll_Killer(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "), input("skąd pochodzisz: "))

        elif x == 5:
            print("Jeśli dla innych elfy są odlutkami i dziwakami, Ty jesteś taki dla innych elfów. Co kompletnie Ci\n"
                  "nie przeszkadza, towarzystwo rozumnych isttot uważasz za stratę czasu. W osadach elfów bywasza bardzo\n"
                  "żadko, tylko gdy to konieczne. Jeśli dotrzeżesz nieproszonego gościa w lesie, albo zostawiasz trupa,\n"
                  "albo nigdy się nie dowie jak blisko otarł się o smierć.")
            player = Ghost_Strider(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "), input("skąd pochodzisz: "))

        elif x == 6:
            print("Kto może równać się we władaniu mocą z Magiem Elfów Wysokiej Rasy? Umiesz spleść wszystkie Wiatry Magii\n,"
                  "Rozmawiasz z aspektami bogów, rozkazujesz stworzeniom, żywiołom i umarłym. Budzisz trwogę nawet w\n"
                  "najpotężniejszych istotach chaosu")
            player = Elf_Mag(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "), input("skąd pochodzisz: "))

        elif x == 7:
            print("Chaos i zniszczenie. Ktoś musi pokazać ci kogo i gdzie masz zabić. Ty z okrutną radością zrobisz resztę.\n"
                  "Tak potężny, nieustraszony wojownik ma status Bersakera - nie podlegasz prawom hordy, możesz bezkarnie\n"
                  " zrobić praktycznie każdą głupotę. Jedyną konsekwencją może być smierć w walce\n")
            player = Bersaker(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "), input("skąd pochodzisz: "))

        elif x == 8:
            print("Rozmawiający z Demonami Szamani mają specjalny status w hordzie. Nie walczą na pierwszej linii. W boju\n"
                  "przywolują demony wchodzące w Bersakerów, a także zrzucają burze ognia na wrogów.\n")
            player = Shaman(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "), input("skąd pochodzisz: "))


        return player
    except(ValueError, NameError, AttributeError):
        print("Przekroczyłeś zakres, lub nie podałaś cyfry. Żeby poprawnie wybrać, podaj cyfrę z zakresu 1 - 8 !!!")


def choosen_next():
    try:
        global player2
        y = int(input("---------------------\n"
        "Drugi gracz, kogo wybierasz?:\n"
        "1 - Palladyn, 2 - ludzki Mag, 3 - Krasnoludzki Atylerzysta,\n"
        "4 - Zabojca Troli, 5 - Leśny Duch, 6 - Elf Mag, 7 - Ork Bersaker, 8 - Szaman Orków: \n "))
        if y == 1:
            print("Jesteś Palladynem, szlachetnym wojownikiem walczącym ze złem. Nie lękasz się nikogo, nie istnieje wróg"
              "zdolny pokonć Wszechmocnego Eru")
            player2 = Palladyn(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "),
                              input("skąd pochodzisz: "))

        elif y == 2:
            print("Ukończyłeś z wyróżnieinem magdeburskie kolegium Magii Kodeksu. Ludzie traktuję cię z nieufnością i strachem,\n"
                  "co nie przeszkada im oferować imperialne dukaty za Twoje usługi.\n")
            player2 = Mag(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "), input("skąd pochodzisz: "))


        elif y == 3:
            print("Spośród masy krasnoludów - wariatów artylerzyści z pewnością są ciekawą grupą. Brak palców, poparzona paskudna\n"
                  "gęba, całkowita lubb częsciowa głuchota. Sprzęt przy którym pracują najczęściej jest bardzo zawodny.\n"
                  "Mimo tych mankamentów jesteś cenionym i poszukiwanym nabytkiem do każdej armii, oddziału najmeników\n"
                  "a także kopalni czy zespołu inzynierów\n")
            player2 = Dwarf_Gunner(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "), input("skąd pochodzisz: "))

        elif y == 4:
            print("Nie ma gorszej dla krasnoluda rzeczy pod słońcem jak okryć się hańbą. Hańba imienia, pamięci, rodu. Niszczy ona\n"
                  "i zatruwa sumienie takiego krasnoluda, a wbrew całemu krasnoludzkiemu chamstwu i grubianstwu, mają oni przecież\n"
                  "poczucie sprawiedliwości, i mocny kręgosłup moralny. Jeśli więc wybierasz tą drogę, nieszczęśniku, masz tylko jeden\n"
                  "cel. Zmazać Twoje zbrodnie piękną, chwalebną śmiercią w samobójczej walce\n")
            player2 = Dwarf_Troll_Killer(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "), input("skąd pochodzisz: "))

        elif y == 5:
            print("Jeśli dla innych elfy są odlutkami i dziwakami, Ty jesteś taki dla innych elfów. Co kompletnie Ci\n"
                  "nie przeszkadza, towarzystwo rozumnych isttot uważasz za stratę czasu. W osadach elfów bywasza bardzo\n"
                  "żadko, tylko gdy to konieczne. Jeśli dotrzeżesz nieproszonego gościa w lesie, albo zostawiasz trupa,\n"
                  "albo nigdy się nie dowie jak blisko otarł się o smierć.\n")
            player2 = Ghost_Strider(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "), input("skąd pochodzisz: "))

        elif y == 6:
            print("Kto może równać się we władaniu mocą z Magiem Elfów Wysokiej Rasy? Umiesz spleść wszystkie Wiatry Magii,\n"
                  "Rozmawiasz z aspektami bogów, rozkazujesz stworzeniom, żywiołom i umarłym. Budzisz trwogę nawet w\n"
                  "najpotężniejszych istotach chaosu\n")
            player2 = Elf_Mag(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "), input("skąd pochodzisz: "))

        elif y == 7:
            print("Chaos i zniszczenie. Ktoś musi pokazać ci kogo i gdzie masz zabić. Ty z okrutną radością zrobisz resztę.\n"
                  "Tak potężny, nieustraszony wojownik ma status Bersakera - nie podlegasz prawom hordy, możesz bezkarnie\n"
                  " zrobić praktycznie każdą głupotę. Jedyną konsekwencją może być smierć w walce\n")
            player2 = Bersaker(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "), input("skąd pochodzisz: "))

        elif y == 8:
            print("Rozmawiający z Demonami Szamani mają specjalny status w hordzie. Nie walczą na pierwszej linii. W boju\n"
                  "przywolują demony wchodzące w Bersakerów, a także zrzucają burze ognia na wrogów.\n")
            player2 = Shaman(input("wpisz imię: "), input("podaj wiek: "), input("podaj płeć: "), input("skąd pochodzisz: "))
        return player2

    except(ValueError, NameError, AttributeError):
        print("Przekroczyłeś zakres, lub nie podałaś cyfry. Żeby poprawnie wybrać, podaj cyfrę z zakresu 1 - 8 !!!")






