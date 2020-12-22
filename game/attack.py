from building import Building
from troop import Troop
from player import Player


class Attack:

    def __init__(self, attacker, defender):
        self.tmp_attacker = attacker
        self.attacker = attacker
        self.pas = Player
        self.pas = attacker
        self.defender = defender
        self.troops = Troop()
        self.buildings = Building()

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
            for i in player.buildings:
                if i['place'] == str(place):
                    i['hp'] = report

    def building_damage(self, code, attacker, defender):
        for i in defender.buildings:
            if i['building'] == code:
                main_damage = i['damage']
                for j in attacker.troops:
                    if j['code'] == 'T' and j['count'] != 0 and j['HP'] < i['damage']:
                        while i['damage'] > 0 and j['count'] > 0 and i['damage'] >= j['HP']:
                            j['count'] -= 1
                            i['damage'] -= j['HP']
                    if j['code'] == 'F' and j['count'] != 0 and j['HP'] < i['damage']:
                        while i['damage'] > 0 and j['count'] > 0 and i['damage'] >= j['HP']:
                            j['count'] -= 1
                            i['damage'] -= j['HP']
                    if j['code'] == 'S' and j['count'] != 0 and j['HP'] < i['damage']:
                        while i['damage'] > 0 and j['count'] > 0 and i['damage'] >= j['HP']:
                            j['count'] -= 1
                            i['damage'] -= j['HP']
                i['Damage'] = main_damage

    def tropp_name(self, code):
        for tr in self.troops.troops:
            if code == tr['code']:
                return tr['name']

    def building_name(self, code):
        for cc in self.buildings.buildings:
            if code == cc['code']:
                return cc['name']

    def war_report(self, dead_troops, defender_buildings, outcome):
        retnon = 0
        print("\n\nWar Report : ")
        print("Units Involved: ", end='')
        for i in self.pas.troops:
            if i['count'] != 0:
                retnon += 1
                print('\n' + '\t' + self.tropp_name(i['code']) + " : " + str(i['count']), end='')
        print('None.') if retnon == 0 else print()

        dead_count = 0
        print("Units KIA : ", end='')
        for i in self.pas.troops:
            for j in dead_troops.troops:
                if i['code'] == j['code']:
                    if i['count'] > 0:
                        dead_count += 1
                        print('\n' + '\t' + self.tropp_name(i['code']) + " : " + str(i['count'] - j['count']), end='')
        print('None.') if retnon == 0 else print()

        empty = 0
        for i in defender_buildings.buildings:
            if i['building'] is not None:
                print('[' + i['place'] + '] : ' + self.building_name(i['building']) + ' : ' +
                      str(i['hp']) + ' / ' + str(i['mhp']))
                empty += 1
            else:
                continue
        if empty == 0:
            print("None.")

        if outcome == 'win':
            print("Outcome : WIN.")
        else:
            print("Outcome : DEFEAT.")
        print('\n')

    def start(self):
        global possible
        possible = False
        attacker = self.attacker
        if len(self.defender.map[0][0]) == 3:
            code = self.defender.map[0][0][2]
            cal = self.calculate_damage(code)
            troops_damage = cal[0]
            building_hp = cal[2]
            res = self.check_attack_to(troops_damage, building_hp)
            self.building_damage(code, self.attacker, self.defender)
            if res == 0:
                self.handle_building_hp(self.defender, 0, 0)
                possible = True
            else:
                self.handle_building_hp(self.defender, res, 0)
                possible = False
                self.war_report(self.attacker, self.defender, 'looser')
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
            self.building_damage(code, self.attacker, self.defender)
            if res == 0:
                self.handle_building_hp(self.defender, 0, 1)
                possible = True
            else:
                self.handle_building_hp(self.defender, res, 1)
                possible = False
                self.war_report(self.attacker, self.defender, 'looser')
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
            self.building_damage(code, self.attacker, self.defender)
            if res == 0:
                possible = True
                self.handle_building_hp(self.defender, 0, 2)
            else:
                possible = False
                self.handle_building_hp(self.defender, res, 2)
                self.war_report(self.attacker, self.defender, 'looser')
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
            self.building_damage(code, self.attacker, self.defender)
            if res == 0:
                possible = True
                self.handle_building_hp(self.defender, 0, 5)
            else:
                possible = False
                self.handle_building_hp(self.defender, res, 5)
                self.war_report(self.attacker, self.defender, 'looser')
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
            self.building_damage(code, self.attacker, self.defender)
            if res == 0:
                possible = True
                self.handle_building_hp(self.defender, 0, 8)
            else:
                possible = False
                self.handle_building_hp(self.defender, res, 8)
                self.war_report(self.attacker, self.defender, 'looser')
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
            self.building_damage(code, self.attacker, self.defender)
            if res == 0:
                possible = True
                self.handle_building_hp(self.defender, 0, 7)
            else:
                possible = False
                self.handle_building_hp(self.defender, res, 7)
                self.war_report(self.attacker, self.defender, 'looser')
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
            self.building_damage(code, self.attacker, self.defender)
            if res == 0:
                possible = True
                self.handle_building_hp(self.defender, 0, 6)
            else:
                possible = False
                self.handle_building_hp(self.defender, res, 6)
                self.war_report(self.attacker, self.defender, 'looser')
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
            self.building_damage(code, self.attacker, self.defender)
            if res == 0:
                possible = True
                self.handle_building_hp(self.defender, 0, 3)
            else:
                possible = False
                self.handle_building_hp(self.defender, res, 3)
                self.war_report(self.attacker, self.defender, 'looser')
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
                self.war_report(self.attacker, self.defender, 'win')
                return 'win'
            else:
                self.handle_building_hp(self.defender, res, 4)
                self.war_report(self.attacker, self.defender, 'looser')
                return 'loose'
