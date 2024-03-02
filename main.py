import time
import random
import rock_paper_scissor as rps
import guess_number as gn
import palidrome as pali
import puzzle as puzzle

class GameSeries:        

    @staticmethod
    def start_game_series():
        print(
            '''
            Welcome to Our Series of Games \n
            Choose which game you want to play \n
            1. Rock, Paper, Scissors
            2. Guess the number game
            3. Palindrome
            4. Puzzle
            5. Exit  
            ''')
        while True:
            service = (input("Enter a number: "))
            if service == '1':
                rps.start_game()
                break
            elif service == '2':
                gn.start_game()
                break
            elif service == '3':
                print("Enter a string: ")
                string = input()
                print(pali.is_palindrome(string))
                break
            elif service == '4':
                puzzle.start_game()
                break
            elif service == '5':
                print("Exit")
                break
            else:
                print('''
                       __________________________
                      |                          |
                      |  Enter a valid number!!  |
                      |__________________________|
                      
                      ''')

if __name__ == "__main__":
    GameSeries.start_game_series()
    
