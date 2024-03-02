#This is 'Guess the number' game

import random
import math
def start_game():
    while True:

        print()
        print("\t\t\t\t *** Welcome to 'GUESS THE NUMBER' game ***")
        print()

        lower = int(input("Enter lower range: "))
        upper = int(input("Enter upper range: "))

        if lower == upper:
            print()
            print("Sorry! The lower and upper number can't same.")
            print()
            exit()

        if lower < upper:

            number = random.randint(lower,upper)
            max_chance = max_guesses = math.ceil(math.log2(upper - lower + 1))
            chance = max_chance

            for _ in range (chance):
                print()
                print(f"You have {chance} chance(s) left")
                print()
                user_num = int(input("Enter your guess: "))

                if user_num == number:
                    print()
                    print("Congratulations! You guessed correct.")
                    break
                elif user_num < number:
                    print()
                    print("You guessed low. Try guessing a higher number")
                elif user_num > number:
                    print()
                    print("You guessed high. Try guessing a lower number")
                
                chance -= 1

            if chance == 0:
                print()
                print("Sorry! You couldn't guess the number.")

        else:
            print()
            print("Wrong input. The lower number is not lower than the upper number")
        
        print()
        replay = input("Enter 'y' if you want to play again: ")
        print()
        if replay.lower() != 'y':
            break