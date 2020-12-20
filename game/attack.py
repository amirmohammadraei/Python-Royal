

class Attack:

    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def start(self):
        total_troops_damage = 0
        for i in self.attacker.troops:
            total_troops_damage += i['count'] * i['Damage']

        if len(self.defender.map[0][0]) == 3:
            pass
        elif len(self.defender.map[0][0]) == 1:
            pass
        else:
            print("Something went wrong.")

        if len(self.defender.map[0][1]) == 3:
            pass
        elif len(self.defender.map[0][1]) == 1:
            pass
        else:
            print("Something went wrong.")

        if len(self.defender.map[0][2]) == 3:
            pass
        elif len(self.defender.map[0][2]) == 1:
            pass
        else:
            print("Something went wrong.")

        if len(self.defender.map[1][2]) == 3:
            pass
        elif len(self.defender.map[1][2]) == 1:
            pass
        else:
            print("Something went wrong.")

        if len(self.defender.map[2][2]) == 3:
            pass
        elif len(self.defender.map[2][2]) == 1:
            pass
        else:
            print("Something went wrong.")

        if len(self.defender.map[2][1]) == 3:
            pass
        elif len(self.defender.map[2][1]) == 1:
            pass
        else:
            print("Something went wrong.")

        if len(self.defender.map[2][0]) == 3:
            pass
        elif len(self.defender.map[2][0]) == 1:
            pass
        else:
            print("Something went wrong.")

        if len(self.defender.map[1][0]) == 3:
            pass
        elif len(self.defender.map[1][0]) == 1:
            pass
        else:
            print("Something went wrong.")

        if len(self.defender.map[1][1]) == 3:
            pass
        elif len(self.defender.map[1][1]) == 1:
            pass
        else:
            print("Something went wrong.")
