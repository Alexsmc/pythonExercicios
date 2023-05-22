#from graphics import Canvas
from random import randint
from time import sleep

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
ELEMENTS = ("PAPER", "SCISSORS", "ROCK", "LIZARD", "SPOCK")


def main():
    # canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO: your code here!
    players_list = []
    repeat = 'Y'
    while repeat in 'yY':
        player_name = str(input("What's your name?: ")).strip().capitalize()
        PLAYER_SCORE = 0
        while True:
            print(f'{player_name} has {PLAYER_SCORE} wins')
            cpu = randint(0, 4)
            print('''CHOSE YOUR WEPON
            [0] PAPER
            [1] SCISSORS
            [2] ROCK
            [3] LIZARD
            [4] SPOCK''')
            p1 = int(input('Choice: '))
            while (p1 < 0) or (p1 > 4):
                print('Try again!!')
                p1 = int(input('Choice: '))
            print('GET READY...')
            sleep(0.8)
            print('GO!!')
            print('=' * 40)
            print(f'{player_name}: {ELEMENTS[p1]} X {ELEMENTS[cpu]}: COMPUTER ')
            if cpu == p1:
                print('DRAW')
            else:
                if cpu == 0:  # paper
                    if (p1 == 2) or (p1 == 4):
                        print('lose')
                        break
                    else:
                        print('win')
                        PLAYER_SCORE += 1
                elif cpu == 1:  # scissors
                    if (p1 == 0) or (p1 == 3):
                        print('lose')
                        break
                    else:
                        print('win')
                        PLAYER_SCORE += 1
                elif cpu == 2:  # rock
                    if (p1 == 1) or (p1 == 3):
                        print('lose')
                        break
                    else:
                        print('win')
                        PLAYER_SCORE += 1
                elif cpu == 3:  # Lizard
                    if (p1 == 0) or (p1 == 4):
                        print('lose')
                        break
                    else:
                        print('win')
                        PLAYER_SCORE += 1
                elif cpu == 4:  # Spock
                    if (p1 == 1) or (p1 == 2):
                        print('lose')
                        break
                    else:
                        print('win')
                        PLAYER_SCORE += 1
            print('=' * 30)
        print(f'{player_name} finished with: {PLAYER_SCORE} wins')
        print('end Game')
        players_list.append(player_name)
        players_list.append(PLAYER_SCORE)
        print('=-'*20)
        print(f'{"RECORDS":^40}')
        place = 0
        for pos in range(0,len(players_list)):
            if pos%2==0:
                place +=1
                print(f'{place}° - {players_list[pos]:.<30}', end='')
            else:
                print(f' {players_list[pos]} WINS')
        print('-='*20)
        repeat = input('Try Again? [Y/N]: ').strip().upper()
        while repeat not in 'yYnN':
            repeat = input('Try Again? [Y/N]: ').strip().upper()

if __name__ == '__main__':
    main()