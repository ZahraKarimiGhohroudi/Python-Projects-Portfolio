"""
    Rock Paper Scissors game
    Author : Zahra Karimi Ghohroudi
    Date : 2026-10-13
    """

import random


class RockPaperScissors():
    """
        Main class for the game Rock, Paper, Scissors 🪨📄✂️
        :param player: refers to each player: a Player object
    """
    __choices = ['Rock', 'Paper', 'Scissors']
    
    def __init__(self, player: "Player"):
        self.player = player

    def get_player_choice(self) -> str:
        """
        Method to get the user's choice.
        :return: User's choice as a string
        """
        user_choice: str = input(f"Enter your choice {RockPaperScissors.__choices} :\n").strip().capitalize()
        
        if user_choice in RockPaperScissors.__choices:
            print(f"You : {user_choice}", end = " | ")
            return user_choice
        
        print("Invalid choice.")
        print(f"You must select from {RockPaperScissors.__choices}")
        return self.get_player_choice()
    
    def get_computer_choice(self) -> str:
        """
        Method to select the computer's choice.
        :return: Computer's choice
        """
        computer_choice = random.choice(RockPaperScissors.__choices)
        print(f"Computer : {computer_choice}")
        return computer_choice
    
    def decide_winner(self, user:str, computer:str)-> str: 
        """
        Method to decide game winner based on the rules.
        :param user: The user's choice
        :param computer: The computer's choice
        :return: Game outcome 
        """
        wins_combination = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
        if user == computer:
            return 'tie'
        if wins_combination[user] == computer:
            return 'player'
        return 'computer'
    
    def play(self):
        """Main method to play game"""
        print("(●ˇ∀ˇ●)")
        print(f"Let's play {self.player.player_name}🎮")
        
        user_choice: str = self.get_player_choice()
        computer_choice: str = self.get_computer_choice()
        
        result: str = self.decide_winner(user_choice, computer_choice)
        
        if result == 'player':
            self.player.add_point()
            print("Congratulations! You won🎉!")
        elif result == 'computer':
            print('Oh no! You lost this round')
        else :
            print("It's a Tie")


class Player():
    """
    Class for players that stores their scores
    """
    __counter = 100000
    def __init__(self, name: str):
        self.player_name = name
        Player.__counter += 1
        self.__id = Player.__counter 
        self.score = 0
    
    def get_id(self):
        return self.__id
    
    def add_point(self):
        """Add one point to the player's score."""
        self.score += 1


def main():
    print('-'*40)
    print("Welcome to Rock-Paper-Scissors game 🪨 📄✂️")
    name = input("What's your name? ")
    player = Player(name)
    game = RockPaperScissors(player)
    print('-'*40)
    print(f"Hello {player.player_name} 💕 ")
    print("Have a nice game, I wish you luck!")
    game.play()

    while True:        
        print('-'*40)
        print(f"Your score is {player.score}")
        print("1. Play Again")
        print("2. Exit")
        choice = input("What do you want? (1 or 2): ")
        
        if choice == '1' :
            game.play()
            
        elif choice == '2':
            print("Goodbye")
            break
            
        else :
            print("This is not a valid number, try again!")

if __name__ == '__main__':
    main()
