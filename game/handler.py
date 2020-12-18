from player import Player
from building import Building
from troop import Troop
from random import *


class Handler:
    buildings = Building()
    troops = Troop()

    def __init__(self, player):
        self.Player = player

    def building_name(self, code):
        for cc in self.buildings.buildings:
            if code == cc['code']:
                return cc['name']

    def tropp_name(self, code):
        for tr in self.troops.troops:
            if code == tr['code']:
                return tr['name']

    def print_player_money(self, player_money):
        if player_money == 0:
            print("You have no more coin.")
        elif player_money == 1:
            print("You have " + str(player_money) + ' coin.')
        else:
            print("You have " + str(player_money) + ' coins.')

    def print_menu(self, player):
        print('player' + str(player) + ' menu: \n'
                                       '1.Buildings construction \n'
                                       '2.Units Training \n'
                                       '3.Show My Map and Army \n'
                                       '4.DONE \n'
                                       'Choose your option: ', end='')

    def check_enough_money(self, buildings_name, player_money):
        for build in self.buildings.buildings:
            if build['code'] == buildings_name:
                if player_money - build['price'] >= 0:
                    return build['price'], build['HP'], build['Damage']
                else:
                    return False

    def print_player_money(self, player_money):
        if player_money == 0:
            print("You have no more coin.")
        elif player_money == 1:
            print("You have " + str(player_money) + ' coin.')
        else:
            print("You have " + str(player_money) + ' coins.')

    map = Player.buildings
    player_troops = Player.troops
    start = 0

    def menu(self, turn):
        while True:
            self.print_menu(turn)
            choice = input()
            if choice == '1':
                for i in Player.map:
                    print(i)
                print("Buildings Present : ")
                empty = 0
                for i in self.map:
                    if i['building'] is not None:
                        print('[' + i['place'] + '] : ' + self.building_name(i['building']) + ' : ' +
                              str(i['hp']) + ' / ' + str(i['mhp']))
                        empty += 1
                    else:
                        continue
                if empty == 0:
                    print("None.")

                a = input("Enter your building expression :")
                if a == 'back':
                    print("back to menu")
                    continue
                else:
                    try:
                        if len(a) == 1 and 0 <= int(a) < 9:
                            print("Your chosen option is to repair building in place=" + a)
                            for i in self.map:
                                if a == i['place']:
                                    if i['building'] is not None:
                                        if i['mhp'] != i['hp']:
                                            res = self.check_enough_money(i['building'], self.Player.money)
                                            if res is False:
                                                print("You don't have enough money to repair your building.", end=' ')
                                                self.print_player_money(self.Player.money)
                                            else:
                                                self.Player.money -= int(res[0])
                                                print("Repair completed successfully.")
                                                self.print_player_money(self.Player.money)
                                        else:
                                            print("This building is not damaged, so no need to repair.")
                                    else:
                                        print("This place is empty so you can't repair anything.")
                        elif len(a) == 3 and a[1] == ' ' and a[0] in ['C', 'T', 'S', 'B'] \
                                and int(a[2]) in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                            if int(a[2]) == 4:
                                print("You cant build in main building.")
                            elif a[0] == 'C' and int(a[2]) != 4:
                                print("Main building can not be built in any place except place 4.")
                            else:
                                for i in self.map:
                                    if i['place'] == a[2]:
                                        if i['building'] is None or i['hp'] == 0:
                                            res = self.check_enough_money(a[0], self.Player.money)
                                            if res is False:
                                                print("You don't have enough money build your building hear.", end=' ')
                                                self.print_player_money(self.Player.money)
                                            else:
                                                self.Player.money -= res[0]
                                                i['building'] = a[0]
                                                i['hp'] = res[1]
                                                i['mhp'] = res[1]
                                                i['damage'] = res[2]
                                                pos = int(a[2])
                                                length = len(Player.map[int(pos / 3)][int(pos % 3)])
                                                if length == 1:
                                                    Player.map[int(pos / 3)][int(pos % 3)] += '-' + a[0]
                                                else:
                                                    Player.map[int(pos / 3)][int(pos % 3)] = a[2] + '-' + a[0]
                                                for p in Player.map:
                                                    print(p)
                                                # print(player1.money)
                                                for m in self.map:
                                                    if m['building'] is not None:
                                                        print('[' + m['place'] + '] : ' + self.building_name(m['building']) +
                                                              ' : ' + str(m['hp']) + ' / ' + str(m['mhp']))
                                                        empty += 1
                                                print("Your request has been successfully done.")
                                                self.print_player_money(self.Player.money)
                                        else:
                                            print("This place is full, you can't add building hear.")
                        else:
                            print("Enter valid input(s).")
                    except ValueError:
                        print("Enter valid input(s).")

            elif choice == '2':
                retnon = 0
                print("Troops available in your army: ", end='')
                for i in self.player_troops:
                    if i['count'] != 0:
                        retnon += 1
                        print('\n' + '\t' + self.tropp_name(i['code']) + " : " + str(i['count']), end='')
                print('None.') if retnon == 0 else print()
                opt2 = input("Enter your troops expression: ")
                if a == 'back':
                    print("back to menu")
                    continue
                if opt2[0] in ['S', 'T', 'F'] and opt2[1] == ' ' and int(opt2[2]) > 0:
                    count = 2
                    num = ''
                    while True:
                        try:
                            num += str(int(opt2[count]))
                            count += 1
                        except IndexError:
                            count = 2
                            break
                        except ValueError:
                            print("Enter valid inputs.")
                            break_point = True
                            count = 2
                            break
                    try:
                        if break_point is True:
                            continue
                    except NameError:
                        pass

                    tedad = int(num)
                    for i in self.troops.troops:
                        if i['code'] == opt2[0]:
                            price = i['price']
                            fee = int(price) * tedad
                            if self.Player.money - fee >= 0:
                                for w in self.Player.troops:
                                    if w['code'] == i['code']:
                                        w['count'] += int(opt2[2])
                                self.Player.money -= fee
                                print("Troops added to your army.")
                                self.print_player_money(self.Player.money)
                            else:
                                print("You don't have enough money.", end=' ')
                                self.print_player_money(self.Player.money)
                else:
                    print("Enter valid inputs.")

            elif choice == '3':
                print("\n\n************ MAP ************")
                for i in Player.map:
                    print(i)
                print()
                empty = 0
                for i in self.map:
                    if i['building'] is not None:
                        print('[' + i['place'] + '] : ' + self.building_name(i['building']) + ' : ' +
                              str(i['hp']) + ' / ' + str(i['mhp']))
                        empty += 1
                    else:
                        continue
                if empty == 0:
                    print("None.")
                print("\n\n************ ARMY ************")
                retnon = 0
                print("Troops available in your army: ", end='')
                for i in self.player_troops:
                    if i['count'] != 0:
                        retnon += 1
                        print('\n' + '\t' + self.tropp_name(i['code']) + " : " + str(i['count']), end='')
                print('None.') if retnon == 0 else print()
                print('\n')
            elif choice == '4':
                print("Done!")
                break
            else:
                print("Please enter valid input.")
