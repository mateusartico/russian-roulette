import random
import os
import time
import sys

def timer(secs):
    for s in range(secs):
        head()
        print(f'\033[32m[!] Starting in {secs - s}...\033[m')
        time.sleep(1)
    start()

def press_enter():
    try:
        input("\n[!] Press Enter to restart... ")
    except(KeyboardInterrupt):
        exit_game()

def input_int():
    while True:
        try:
            number = int(input("> "))
        except(ValueError, TypeError):
            print('\033[31mThis is not an option\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[33m\n[!] Bye\033[m')
            sys.exit()
        else:
            return number

def gun_update(bullets):
    global gun1
    global gun2
    global gun3

    gun1 = f'''
      +--^----------,--------,-----,--------^-,
      | |||||||||   `--------'                O        {bullets}/17
      `+---------------------------^----------|
        `\_,---------,---------,--------------'
          / XXXXXX /'|       /'
         / XXXXXX /  `\    /'
        / XXXXXX /`-------'
       / XXXXXX /
      / XXXXXX /
     (________(                
      `------'
    '''
    gun2 = f'''
  +--^----------,--------,-----,--------^-,
  | |||||||||   `--------'                XXXXO        {bullets}17
  `+---------------------------^----------|----
        `\_,---------,---------,--------------'
          / XXXXXX /'/       /'
         / XXXXXX / '|     /'
        / XXXXXX /`-------'
       / XXXXXX /
      / XXXXXX /
     (________(                
      `------' 
    '''

    gun3 = f'''
      +--^----------,--------,-----,--------^-,\033[33m|/\033[m
      | |||||||||   `--------'                O\033[33m---\033[m     {bullets}/17
      `+---------------------------^----------|\033[33m|\ \033[m  
        `\_,---------,---------,--------------'
          / XXXXXX /'|       /'
         / XXXXXX /  `\    /'
        / XXXXXX /`-------'
       / XXXXXX /
      / XXXXXX /
     (________(                
      `------' 
    '''

def start():
    bullets = 17
    gun_update(bullets)
    for n in range(3):
        gun_update(bullets)
        head()
        print(gun1)
        time.sleep(1)
        head()
        print(gun2)
        time.sleep(0.05)
        head()
        print(gun3)
        time.sleep(0.1)
        bullets -= 1
    gun_update(bullets)
    head()
    print(gun1)
    time.sleep(1)
    head()
    print("You pulled the trigger 3 times... But...")
    time.sleep(2)
    if random.randint(1, 17) in [1, 2, 3]:
        print("\033[31mYou don't survived\033[m")
        time.sleep(1)
        shutdown()
    else:
        print("\033[32mYou survived\033[m")
        press_enter()

def menu(itens):
    head()
    c = 1
    for i in itens:
        print(f'{c}. {i}')
        c += 1

    selection = input_int()
    while True:
        if (selection > c) or (selection < 0):
            print('\033[31mThis is not an option\033[m')
            selection = input_int()
        elif selection == 1:
            timer(3)
            break
        else:
            exit_game()

def head():
    title = '''
                           .__                                    .__          __    __          
_______ __ __  ______ _____|__|____    ____   _______  ____  __ __|  |   _____/  |__/  |_  ____  
\_  __ \  |  \/  ___//  ___/  \__  \  /    \  \_  __ \/  _ \|  |  \  | _/ __ \   __\   __\/ __ \ 
 |  | \/  |  /\___ \ \___ \|  |/ __ \|   |  \  |  | \(  <_> )  |  /  |_\  ___/|  |  |  | \  ___/ 
 |__|  |____//____  >____  >__(____  /___|  /  |__|   \____/|____/|____/\___  >__|  |__|  \___  >
                  \/     \/        \/     \/                                \/                \/ 
    '''
    os.system('cls')
    print(f'\033[1m{'-' * 97}\033[m')
    print(f'\033[1m{'-' * 97}\033[m')
    print(f'\033[34m{title}\033[m')
    print(f'\n\033[1m{"By Mateus Artico".rjust(97, " ")}\033[m')
    print(f'\033[1m{"https://github.com/mateusartico".rjust(97, " ")}\033[m')
    print('\033[31m-\033[m' * 97)
    print('\033[31m-\033[m' * 97)

def exit_game():
    os.system('cls')
    head()
    print("\033[33m[.] Bye bye\033[m")
    sys.exit()

def shutdown():
    os.system('shutdown /s /t 1')

def russian_roulette():
    while True:
        menu(['Play', 'Exit'])

if __name__ == '__main__':
    russian_roulette()