#from graphics import Canvas
import json
from random import randint
from time import sleep

#CANVAS_WIDTH = 400
#CANVAS_HEIGHT = 400
ELEMENTS = ("PAPER", "SCISSORS", "ROCK", "LIZARD", "SPOCK")


def main():
    # canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    #player_list = []
    players = [0, 'Nome']
    repeat = 'Y'
    with open('records.txt', 'r', encoding="utf-8") as file:
        player_list = json.load(file)

    while repeat in 'yY':
        player_name = str(input("What's your name?: ")).strip().capitalize()
        PLAYER_SCORE = 0
        while True:
            print(f'{player_name} has {PLAYER_SCORE} wins')
            cpu = randint(0, 4)
            print('''CHOOSE YOUR WEAPON
            [0] PAPER
            [1] SCISSORS
            [2] ROCK
            [3] LIZARD
            [4] SPOCK''')
            while True:
                try:
                    p1 = int(input('Choice: '))
                    if not 0 <= p1 <= 4:
                        raise ValueError("Out of the range")
                except ValueError as e:
                    print("Invalid Value:", e)
                else:
                    break
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
        print('GAME OVER')
        players[1] = player_name
        players[0] = PLAYER_SCORE
        player_list.append(players[:])
        player_list.sort(reverse=True)
        if len(player_list) > 10:
            player_list.pop()
        with open('records.txt', 'w') as file:
            json.dump(player_list, file)
        print('=-'*30)
        print(f'{"RECORDS":^40}')
        count = 0
        for p in player_list:
            count += 1
            print(f'{count} - {p[1]:.<1}', '-'*20, f'{p[0]:>1}')
        print('-='*30)
        repeat = input('Try Again? [Y/N]: ').strip().upper()
        while repeat not in 'yYnN':
            repeat = input('Try Again? [Y/N]: ').strip().upper()


if __name__ == '__main__':
    main()