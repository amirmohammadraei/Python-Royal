from player import Player
from building import Building
from handler import Handler
from troop import Troop
from attack import Attack
from random import *


def menu(player):
    print('player' + str(player) + ' menu: \n'
                                   '1.Buildings construction \n'
                                   '2.Units Training \n'
                                   '3.Show My Map and Army \n'
                                   '4.DONE \n'
                                   'Choose your option: ', end='')


def change_player(time):
    if time == 1:
        return 2
    elif time == 2:
        return 1


def check_enough_money(buildings_name, player_money):
    for build in buildings.buildings:
        if build['code'] == buildings_name:
            if player_money - build['price'] >= 0:
                return build['price'], build['HP'], build['Damage']
            else:
                return False


def print_player_money(player_money):
    if player_money == 0:
        print("You have no more coin.")
    elif player_money == 1:
        print("You have " + str(player_money) + ' coin.')
    else:
        print("You have " + str(player_money) + ' coins.')


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
    while True:
        nickname1 = input("Player1 please enter your nickname: ")
        if len(nickname1) == 0:
            continue
        else:
            break
    while True:
        nickname2 = input("Player2 please enter your nickname: ")
        if len(nickname2) == 0:
            continue
        else:
            break
    player1 = Player(nickname1, 50000)
    player2 = Player(nickname2, 50000)
    print('\n')

    count = 0
    turn = randint(1, 2)
    print("Player" + str(turn) + " you should start.")
    while count != 3:
        count += 1
        if turn == 1:
            var1 = Handler(player1).menu(1)
            var2 = Handler(player2).menu(2)
            result = Attack(player1, player2).start()
            if result == 'win':
                player1.successful_attacks += 1
                turn = 1
            else:
                turn = 2

        elif turn == 2:
            var2 = Handler(player2).menu(2)
            var1 = Handler(player1).menu(1)
            result = Attack(player2, player1).start()
            if result == 'win':
                player2.successful_attacks += 1
                turn = 2
            else:
                turn = 1

        else:
            print("Something went wrong. Try again.")

    if player1.successful_attacks > player2.successful_attacks:
        player1.money += player2.money
        print("Player1 is winner.")

    elif player1.successful_attacks < player2.successful_attacks:
        player2.money += player1.money
        print("Player2 is winner.")

    else:
        print("After a hard match, we have no winner.\n  \t Good luck :) ")
