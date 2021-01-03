import random
import time
from battle import fight
from create_team import create_first_team, create_second_team, actualy_1_fighter, actualy_2_fighter

def starcie_teamow(team_one, team_two, actualy_1_fighter, actualy_2_fighter):
    round = 1
    while True:
        print(f"Starcie {round} !")
        if random.randint(0, 1) == 0:
            print(f"walkę zaczyna {team_one.team_name}!")
            fight(actualy_1_fighter, actualy_2_fighter)
        else:
            print(f"walkę zaczyna {team_two.team_name}!")
            fight(actualy_2_fighter, actualy_1_fighter)

        time.sleep(5)
        round += 1

starcie_teamow(create_first_team(), create_second_team(), actualy_1_fighter(), actualy_2_fighter())


