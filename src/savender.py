import pyfiglet  
from pyfiglet import Figlet
from termcolor import colored, cprint
import music
import movies 
import time

userInput = 0

def ascii_title():
    ascii_format = Figlet(font='trek',justify="center")
    ascii_title = ascii_format.renderText('Savender')
    print("\n")
    print(colored(ascii_title, 'red'))

def menu():
    menu = "1. Get Music Recs!"
    x = menu.center(65)
    print(colored(x, 'green'))
    menu = "2. Get Movie Recs!"
    x = menu.center(65)
    print(colored(x, 'green'))
    menu = "3. Terminate Program"
    x = menu.center(65)
    print(colored(x, 'green'))

def menu_loop():
    ascii_title()
    print("\n")
    menu()

def movie_recs():
    movies.main()

def music_recs():
    music.main()

ascii_title()
print("Welcome!\n".center(65))
time.sleep(0.8)
menu()
while(userInput != 3):
    userInput = int(input(colored("\nEnter a number to choose: ", 'green')))
    if (userInput == 1):
        music_recs()
        menu_loop()
    elif (userInput == 2):
        movie_recs()
        menu_loop()
    elif (userInput == 3):
        print(colored("\nGoodbye!".center(65), 'green'))
        break
    else:
        print("Enter a valid number or choice!")
        menu_loop()



'''
custom_fig = Figlet(font='trek',justify="center")
print(custom_fig.renderText('Savender'))
text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text.center(60))
cprint('Hello, World!', 'green', 'on_red')
test = input("Press Enter!")
'''