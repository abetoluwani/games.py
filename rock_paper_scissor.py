#This is rock, paper, scissor game

#importing 'random' to generate a random number
import random

def start_game():   
    while True:

        #Preparing welcome screen
        print()
        print("\t\t\t\t***Welcome! This is rock, paper, and scissor game***")
        print()
        print("\t\t\tThe Rules Are Simple: Rock beats scissor, Scissor beats paper, and Paper beats rock")
        print()
        print ("\t***To choose Rock enter 1***\t\t***For Paper enter 2***\t\t***For Scissor enter 3***")
        print()

        #Taking input from user and printing their choice

        try:
            a = int(input("Choose a number from 1 to 3: "))
            print()

            if a==1:
                print("You chose rock")
            elif a==2:
                print("You chose paper")
            elif a==3:
                print("You chose scissor")
            else:
                print("Invalid Input. The program is terminated.")
                print()
                exit()

            print()

            #Generating random number for computer and printing its choice
            b = random.randint(1, 3)
            if b==1:
                print("Computer chose rock")
            elif b==2:
                print("Computer chose paper")
            elif b==3:
                print("Computer chose scissor")

            print()

            #Applying the rules of the game
            if a==b:
                print("It's a draw.")
            if (a==1 and b==2) or (a==2 and b==3) or (a==3 and b==1):
                print('Sorry! You Lost. Try again.')
            if (a==2 and b==1) or (a==3 and b==2) or (a==1 and b==3):
                print('Congratulations! You Win.')

            print()

        except ValueError:
            print()
            print("You are supposed to enter a integer from 1 to 3")

        print()

        ag = input("Press 'y' if you want to play again: ")
        if ag.upper() != 'Y':
            break
    print()