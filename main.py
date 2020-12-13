from Player.player import Player
from Building.building import Building
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


if __name__ == '__main__':
    print("Hi everyone!")
    nickname1 = input("Player1 please enter your nickname: ")
    nickname2 = input("Player2 please enter your nickname: ")
    player1 = Player(nickname1, 5000000)
    player2 = Player(nickname2, 5000000)
    map1 = Player.buildings
    map2 = Player.buildings
    turn = randint(1, 2)
    start = 0
    print("Player" + str(turn) + " you should start.")
    menu(turn)
    choice = input()
    if choice == '1':
        for i in map1:
            if i['building'] is None:
                print('sa')
            else:
                print(i['place'])
    elif choice == '2':
        print("2")
    elif choice == '3':
        print('3')
    elif choice == '4':
        print('4')
    else:
        print('Invalid choice')
