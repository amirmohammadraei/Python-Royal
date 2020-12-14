from Player.player import Player
from Building.building import Building
from Troop.troop import Troop
from random import *


def menu(player):
    print('player' + str(player) + ' menu: \n'
                                   '1.Buildings construction \n'
                                   '2.Units Training \n'
                                   '3.Show My Map and Army \n'
                                   '4.DONE \n'
                                   'Choose your option: ', end='')


def change_player(turn):
    if turn == 1:
        return 2
    elif turn == 2:
        return 1


def check_enough_money(building_name, player_money):
    for build in buildings.buildings:
        if build['code'] == building_name:
            if player_money - build['price'] >= 0:
                return build['price'], build['HP'], build['Damage']
            else:
                return False


def building_name(code):
    for cc in buildings.buildings:
        if code == cc['code']:
            return cc['name']


def tropp_name(code):
    for tr in troops.troops:
        if code == tr['code']:
            return tr['name']


if __name__ == '__main__':
    print("Hi everyone!")
    buildings = Building()
    troops = Troop()
    nickname1 = input("Player1 please enter your nickname: ")
    nickname2 = input("Player2 please enter your nickname: ")
    player1 = Player(nickname1, 500)
    player2 = Player(nickname2, 5000000)
    map1 = player1.buildings
    map2 = player2.buildings
    troops1 = player1.troops
    troops2 = player2.troops
    turn = randint(1, 2)
    start = 0
    print("Player" + str(turn) + " you should start.")
    while True:
        menu(turn)
        choice = input()
        if choice == '1':
            for i in player1.map:
                print(i)
            print("Buildings Present : ")
            empty = 0
            for i in map1:
                if i['building'] is not None:
                    print('[' + i['place'] + '] : ' + building_name(i['building']) + ' : ' +
                          str(i['hp']) + ' / ' + str(i['mhp']))
                    empty += 1
                else:
                    continue
            if empty == 0:
                print("None.")

            a = input("Enter your building expression :")
            if a == 'back':
                print("back to menu")
            else:
                try:
                    if len(a) == 1 and 0 <= int(a) < 9:
                        print("Your chosen option is to repair building in place=" + a)
                        for i in map1:
                            if a == i['place']:
                                if i['building'] is not None:
                                    if i['mhp'] != i['hp']:
                                        res = check_enough_money(i['building'], player1.money)
                                        if res is False:
                                            print("You don't have enough money to repair your building.")
                                        else:
                                            player1.money -= int(res[0])
                                            print("Repair completed successfully.")
                                            print(player1.money)
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
                            for i in map1:
                                if i['place'] == a[2]:
                                    if i['building'] is None or i['hp'] == 0:
                                        res = check_enough_money(a[0], player1.money)
                                        if res is False:
                                            print("You don't have enough money build your building hear.")
                                        else:
                                            player1.money -= res[0]
                                            i['building'] = a[0]
                                            i['hp'] = res[1]
                                            i['mhp'] = res[1]
                                            i['damage'] = res[2]
                                            pos = int(a[2])
                                            length = len(player1.map[int(pos / 3)][int(pos % 3)])
                                            if length == 1:
                                                player1.map[int(pos / 3)][int(pos % 3)] += '-' + a[0]
                                            else:
                                                player1.map[int(pos / 3)][int(pos % 3)] = a[2] + '-' + a[0]
                                            for p in player1.map:
                                                print(p)
                                            # print(player1.money)
                                            for m in map1:
                                                if m['building'] is not None:
                                                    print('[' + m['place'] + '] : ' + building_name(m['building']) +
                                                          ' : ' + str(m['hp']) + ' / ' + str(m['mhp']))
                                                    empty += 1
                                            print("Your request has been successfully done.")
                                    else:
                                        print("This place is full, you can't add building hear.")
                    else:
                        print("Enter valid input(s).")
                except ValueError:
                    print("Enter valid input(s).")

        elif choice == '2':
            retnon = 0
            print("Troops available in your army: ", end='')
            for i in troops1:
                if i['count'] != 0:
                    retnon += 1
                    print('\n' + '\t' + tropp_name(i['code']) + " : " + str(i['count']), end='')
            print('None.') if retnon == 0 else print()
            opt2 = input("Enter your troops expression: ")

        elif choice == '3':
            print('3')
        elif choice == '4':
            print("Done!")
            break
        else:
            print('Invalid choice')
