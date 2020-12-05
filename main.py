from Player.player import Player
from Building.building import Building
from random import *


def menu(player):
    print('player' + str(player) + ' menu: \n'
                                   '1.Buildings construction 2.Units Training \n'
                                   '3.Show My Map and Army \n'
                                   '4.DONE \n'
                                   'Choose your option:...')


if __name__ == '__main__':
    print("Hi everyone!")
    nickname1 = input("Player1 please enter your nickname: ")
    nickname2 = input("Player2 please enter your nickname: ")
    player1 = Player(nickname1, 5000000)
    player2 = Player(nickname2, 5000000)
    turn = randint(1, 2)
    print("Player" + str(turn) + " you should start.")
    menu(turn)

