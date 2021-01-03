from team import Team
from choose import choosen, choosen_next


def create_first_team():
    global first_team
    first_team = Team(input("Pierwszy grajku, podaj nazwę pierwszej drużyny: "))
    x = int(input("Podaj, ilu zawodników ma mieć Twoja drużuna: "))
    for i in first_team:
        if i.stilalive == False:
            first_team.team_members.remove(i)
            print(f"Ojej! Wyglada na to że {i.name} już nie żyje, i opuszcza {first_team.team_name}")

    while x > 0:
        x -= 1
        first_team.add_members(choosen())

    global actualy_1_fighter
    actualy_1_fighter = first_team.team_members[0]
    return first_team

def actualy_1_fighter():
    return actualy_1_fighter

def create_second_team():
    global second_team
    second_team = Team(input("Drugi grajku, podaj nazwę drugiej drużyny: "))
    y = int(input("Podaj, ilu zawodników ma mieć Twoja drużuna: "))
    for ii in first_team:
        if ii.stilalive == False:
            first_team.team_members.remove(ii)
            print(f"Ojej! Wyglada na to że {ii.name} już nie żyje, i opuszcza {first_team.team_name}")

    while y > 0:
        y -= 1
        second_team.add_members(choosen_next())

    global actualy_2_fighter
    actualy_2_fighter = second_team.team_members[0]
    return second_team

def actualy_2_fighter():
    return actualy_2_fighter