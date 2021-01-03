class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        self.team_members = []

    def add_members(self, member):
        self.team_members.append(member)
        print(self.team_members)

    def team_alive(self):
        if len(self.team_members) > 0:
            return True
        else:
            print(f"{self.team_name}, wyrżeneli drużynę do nogi!!!")
            return False
    
    def __iter__(self):
        return iter(self.team_members)


