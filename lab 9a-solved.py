#ALEJANDRA SILVA

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)


def get_computer_choice():
    return random.choice(choices)

def get_human_choice(player_num):
    choice = input(f"Player {player_num}, pick one of rock, paper, or scissors: ").lower()
    while choice not in choices:
        choice = input(f"Invalid choice. Player {player_num}, pick one of rock, paper, or scissors: ").lower()
    return choice

def determine_winner(p1, p2):
    if p1 == p2:
        return "It's a tie!"
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

class RockPaperScissorsGame:
    def __init__(self, num_human_players):
        self.num_human_players = num_human_players

    def play_once(self):
        if self.num_human_players == 0:
            p1 = get_computer_choice()
            p2 = get_computer_choice()
        elif self.num_human_players == 1:
            p1 = get_human_choice(1)
            p2 = get_computer_choice()
        else:
            p1 = get_human_choice(1)
            p2 = get_human_choice(2)
        print(f"Player 1 chose {p1}, Player 2 chose {p2}.")
        print(determine_winner(p1, p2))

    def play_multiple_games(self, num_games):
        results = {"Player 1 wins": 0, "Player 2 wins": 0, "It's a tie": 0}
        for _ in range(num_games):
            if self.num_human_players == 0:
                p1 = get_computer_choice()
                p2 = get_computer_choice()
            elif self.num_human_players == 1:
                p1 = get_human_choice(1)
                p2 = get_computer_choice()
            else:
                p1 = get_human_choice(1)
                p2 = get_human_choice(2)
            result = determine_winner(p1, p2)
            if result == "Player 1 wins!":
                results["Player 1 wins"] += 1
            elif result == "Player 2 wins!":
                results["Player 2 wins"] += 1
            else:
                results["It's a tie"] += 1
        print(f"Results after {num_games} games: {results}")

def main():
    num_human_players = int(input("Enter the number of human players (0, 1, or 2): "))
    game = RockPaperScissorsGame(num_human_players)
    game.play_once()  # Play a single game
    num_games = int(input("How many games would you like to play in total? "))
    game.play_multiple_games(num_games)  # Play multiple games

if __name__ == "__main__":
    main()
