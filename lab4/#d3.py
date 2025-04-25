
from lab4_2 import play_game
from lab4_1 import game_start1
def startts():
    s = input("Введите число 1 либо 2:")
    if s == '1':
        play_game()
    if s == '2':
        game_start1()
startts()