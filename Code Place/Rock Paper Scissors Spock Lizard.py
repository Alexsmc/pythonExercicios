import json
from random import randint
from time import sleep
import os

ELEMENTS = ("PAPER", "SCISSORS", "ROCK", "LIZARD", "SPOCK")


def main():
    players = [0, 'Nome']

    with open('ranking.txt', 'r', encoding="utf-8") as file:
        player_list = json.load(file)
    print('''THE BIG BANG THEORY JO-KE-PO-LIZ-SPOCK GAME

    CHALLENGE YOUR FRIENDS TO BEAT THESE PREVIOUS PLAYERS''')
    print('=-' * 15)
    print(f'{"RECORDS":^30}')
    for p in player_list:
        print(f'{p[1]:.<1}', '-' * (20 - len(p[1])), f'{p[0]:>1}')
    print('-=' * 15)
    repeat = 'Y'
    while repeat in 'yY':
        print()
        player_name = str(input("WHAT'S YOUR NAME?: ")).strip().capitalize()
        player_score = 0
        while True:
            print('=-' * 15)
            print(f'{player_name}\nWINS: {player_score}')
            print('=-' * 15)
            cpu = randint(0, 4)
            print('''CHOOSE YOUR WEAPON\n[0] PAPER\n[1] SCISSORS\n[2] ROCK\n[3] LIZARD\n[4] SPOCK''')
            print()
            while True:
                try:
                    p1 = int(input('YOUR CHOICE: '))
                    if not 0 <= p1 <= 4:
                        raise ValueError("Out of the range")
                except ValueError as e:
                    print("Invalid Value:", e)
                else:
                    break
            os.system("cls")
            print('GET READY...')
            sleep(0.8)
            print('GO!!')
            print('=' * 20)
            print(f'{player_name}: {ELEMENTS[p1]} X {ELEMENTS[cpu]}: COMPUTER ')
            if cpu == p1:
                print('DRAW')
            else:
                if cpu == 0:  # paper
                    if (p1 == 2) or (p1 == 4):
                        print('YOU LOSE')
                        break
                    else:
                        print('VICTORY!!')
                        player_score += 1
                elif cpu == 1:  # scissors
                    if (p1 == 0) or (p1 == 3):
                        print('YOU LOSE')
                        break
                    else:
                        print('VICTORY!!')
                        player_score += 1
                elif cpu == 2:  # rock
                    if (p1 == 1) or (p1 == 3):
                        print('YOU LOSE')
                        break
                    else:
                        print('VICTORY!')
                        player_score += 1
                elif cpu == 3:  # Lizard
                    if (p1 == 0) or (p1 == 4):
                        print('YOU LOSE')
                        break
                    else:
                        print('VICTORY!')
                        player_score += 1
                elif cpu == 4:  # Spock
                    if (p1 == 1) or (p1 == 2):
                        print('YOU LOSE')
                        break
                    else:
                        print('VICTORY!')
                        player_score += 1
            print('=' * 20)

        # Finishing the game
        print(f'{player_name} finished with: {player_score} wins')
        print('GAME OVER')
        players[1] = player_name
        players[0] = player_score

        # Saving in the list
        player_list.append(players[:])
        player_list.sort(reverse=True)
        if len(player_list) > 10:
            player_list.pop()

        '''ADDING to the file (unfortunately it doesn't save in the site,
           but you can try in your computer.'''
        with open('ranking.txt', 'w') as file:
            json.dump(player_list, file)

        # print the list updated
        print('=-' * 20)
        print(f'{"RECORDS":^30}')
        for p in player_list:
            print(f'{p[1]:.<1}', '-' * (20 - len(p[1])), f'{p[0]:>1}')
        print('-=' * 20)

        # Do you want to try again?
        repeat = input('Try Again? [Y/N]: ').strip().upper()
        while repeat not in 'yYnN':
            repeat = input('Try Again? [Y/N]: ').strip().upper()

    # Closing the game
    print('Thanks for playing')


if __name__ == '__main__':
    main()
