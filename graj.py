from battle import starcie
from choose import choosen, choosen_next
from teams_battle import starcie_teamow
from create_team import create_first_team, create_second_team, actualy_1_fighter, actualy_2_fighter
print("Zastanów sie, czy chcesz zagrać pojedynek 1 vs 2, czy walkę drużyn")
xyz = int(input(" Co wybierasz? 1 - Pojedynek, 2 - Walka drużyn: "))

if xyz == 1:
    starcie(choosen(), choosen_next())

elif xyz == 2:
    starcie_teamow(create_first_team(), create_second_team(), actualy_1_fighter(), actualy_2_fighter())

