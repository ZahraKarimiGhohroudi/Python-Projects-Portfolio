import random
import math
from results import store_results

def start_game(user_id):
    print('-'*20)
    print("Starting new game...")
    print("At first, choose your difficulty level:")
    print("1: Easy (1-1000)")
    print("2: Medium (1000-10000)")
    print("3: Hard (1-100000)")
    print("4: Leave")

    a,b = 0 , math.inf
    
    level = input("Enter your choice (1-4): ")
    print('-'*20)

    while True:
        if level == "1":
            # Easy mode logic
            random_number = random.randint(1, 1000)
            a,b = 1, 1000    
        elif level == "2":
            # Medium mode logic
            random_number = random.randint(1000, 10000)
            a,b = 1000, 10000
        elif level == "3":
            # Hard mode logic
            random_number = random.randint(1, 100000)
            a,b = 1,100000
            
        elif level == "4":
            print("Okay, We backed to main menu.")
            return
        
        else:
            print("Invalid choice. Please try again.")
            continue
        break
    
    guess = None
    number_of_guesses = 0
    
    print('The game is starting...')
    while guess != random_number:
        guess = input("Enter your guess: ")
        
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Please enter a valid number.\nTry again.")
            continue
        number_of_guesses += 1
        
        if guess < a or guess > b:
            print('Oh noo!')
            print(f"Please enter a number between {a} and {b}.")
            continue
        
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
    print("-"*20)
    print("Congratulations! You guessed the number.")
    print(f"you did it with {number_of_guesses} guesses!")
    score = 5000*(int(level)) - number_of_guesses * 100
    print(f"You get {score} points!")
    store_results(user_id, level ,score )
