

class Attack:

    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def start(self):
        total_troops_damage = 0
        for i in self.attacker.troops:
            total_troops_damage += i['count'] * i['Damage']


