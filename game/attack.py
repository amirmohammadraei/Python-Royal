

class Attack:

    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def calculate_damage(self, building_code):
        total_troops_damage = 0
        total_building_damage = 0
        for i in self.attacker.troops:
            total_troops_damage += i['count'] * i['Damage']
        for j in self.defender.buildings:
            if j['building'] == building_code:
                total_building_damage = j['damage']

        return total_troops_damage, total_building_damage

    def start(self):
        if len(self.defender.map[0][0]) == 3:
            code = self.defender.map[0][0][2]
            cal = self.calculate_damage(code)
            print(cal)


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
