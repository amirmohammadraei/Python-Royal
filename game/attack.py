
class Attack:

    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def calculate_damage(self, building_code):
        total_troops_damage = 0
        total_building_damage = 0
        building_hp = 0
        for i in self.attacker.troops:
            total_troops_damage += i['count'] * i['Damage']
        for j in self.defender.buildings:
            if j['building'] == building_code:
                total_building_damage = j['damage']
                building_hp = j['hp']
        print(total_troops_damage, total_building_damage, building_hp)
        return total_troops_damage, total_building_damage, building_hp

    def check_attack_to(self, troops_damage, building_hp):
        if troops_damage > building_hp:
            return 0
        else:
            res = building_hp - troops_damage
            return res

    def handle_building_hp(self, player, report, place):
        if report == 0:
            for i in player.buildings:
                if i['place'] == str(place):
                    i['hp'] = 0
        else:
            print(report)
            for i in player.buildings:
                if i['place'] == str(place):
                    i['hp'] = report


    def start(self):
        global possible
        possible = False
        if len(self.defender.map[0][0]) == 3:
            code = self.defender.map[0][0][2]
            cal = self.calculate_damage(code)
            troops_damage = cal[0]
            building_hp = cal[2]
            res = self.check_attack_to(troops_damage, building_hp)
            if res == 0:
                self.handle_building_hp(self.defender, 0, 0)
                possible = True
            else:
                self.handle_building_hp(self.defender, res, 0)
                possible = False
                return 'loose'
        elif len(self.defender.map[0][0]) == 1:
            possible = True
            pass

        if len(self.defender.map[0][1]) == 3 and possible is True:
            code = self.defender.map[0][1][2]
            cal = self.calculate_damage(code)
            troops_damage = cal[0]
            building_hp = cal[2]
            res = self.check_attack_to(troops_damage, building_hp)
            if res == 0:
                self.handle_building_hp(self.defender, 0, 1)
                possible = True
            else:
                self.handle_building_hp(self.defender, res, 1)
                possible = False
                return 'loose'
        elif len(self.defender.map[0][1]) == 1:
            possible = True
            pass

        if len(self.defender.map[0][2]) == 3 and possible is True:
            code = self.defender.map[0][2][2]
            cal = self.calculate_damage(code)
            troops_damage = cal[0]
            building_hp = cal[2]
            res = self.check_attack_to(troops_damage, building_hp)
            if res == 0:
                possible = True
                self.handle_building_hp(self.defender, 0, 2)
            else:
                possible = False
                self.handle_building_hp(self.defender, res, 2)
                return 'loose'
        elif len(self.defender.map[0][2]) == 1:
            possible = True
            pass

        if len(self.defender.map[1][2]) == 3 and possible is True:
            code = self.defender.map[1][2][2]
            cal = self.calculate_damage(code)
            troops_damage = cal[0]
            building_hp = cal[2]
            res = self.check_attack_to(troops_damage, building_hp)
            print(res)
            if res == 0:
                possible = True
                self.handle_building_hp(self.defender, 0, 5)
            else:
                possible = False
                self.handle_building_hp(self.defender, res, 5)
                return 'loose'
        elif len(self.defender.map[1][2]) == 1:
            possible = True
            pass
        if len(self.defender.map[2][2]) == 3 and possible is True:
            code = self.defender.map[2][2][2]
            cal = self.calculate_damage(code)
            troops_damage = cal[0]
            building_hp = cal[2]
            res = self.check_attack_to(troops_damage, building_hp)
            if res == 0:
                possible = True
                self.handle_building_hp(self.defender, 0, 8)
            else:
                possible = False
                self.handle_building_hp(self.defender, res, 8)
                return 'loose'
        elif len(self.defender.map[2][2]) == 1:
            possible = True
            pass

        if len(self.defender.map[2][1]) == 3 and possible is True:
            code = self.defender.map[2][1][2]
            cal = self.calculate_damage(code)
            troops_damage = cal[0]
            building_hp = cal[2]
            res = self.check_attack_to(troops_damage, building_hp)
            if res == 0:
                possible = True
                self.handle_building_hp(self.defender, 0, 7)
            else:
                possible = False
                self.handle_building_hp(self.defender, res, 7)
                return 'loose'
        elif len(self.defender.map[2][1]) == 1:
            possible = True
            pass


        if len(self.defender.map[2][0]) == 3 and possible is True:
            code = self.defender.map[2][0][2]
            cal = self.calculate_damage(code)
            troops_damage = cal[0]
            building_hp = cal[2]
            res = self.check_attack_to(troops_damage, building_hp)
            if res == 0:
                possible = True
                self.handle_building_hp(self.defender, 0, 6)
            else:
                possible = False
                self.handle_building_hp(self.defender, res, 6)
                return 'loose'
        elif len(self.defender.map[2][0]) == 1:
            possible = True
            pass

        if len(self.defender.map[1][0]) == 3 and possible is True:
            code = self.defender.map[1][0][2]
            cal = self.calculate_damage(code)
            troops_damage = cal[0]
            building_hp = cal[2]
            res = self.check_attack_to(troops_damage, building_hp)
            if res == 0:
                possible = True
                self.handle_building_hp(self.defender, 0, 3)
            else:
                possible = False
                self.handle_building_hp(self.defender, res, 3)
                return 'loose'
        elif len(self.defender.map[1][0]) == 1:
            possible = True
            pass


        if len(self.defender.map[1][1]) == 3 and possible is True:
            code = self.defender.map[1][1][2]
            cal = self.calculate_damage(code)
            troops_damage = cal[0]
            building_hp = cal[2]
            res = self.check_attack_to(troops_damage, building_hp)
            if res == 0:
                self.handle_building_hp(self.defender, 0, 4)
                return 'win'
            else:
                self.handle_building_hp(self.defender, res, 4)
                return 'loose'

