# Script: rock_paper_scissors.py
# Description: Rock, Paper, Scissors Game
# Author: Mohammed Abdul Raqeeb
# Date: 22/06/2024

try:
    from colorama import Fore, Style
except ImportError:
    print("This script requires the 'colorama' module.\nPlease install it using 'pip install colorama' and try again.")
    exit(1)

from random import choice
from time import sleep


# Define colors and styles
blue = Fore.BLUE
cyan = Fore.CYAN
green  = Fore.GREEN
magenta = Fore.MAGENTA
red = Fore.RED
yellow = Fore.YELLOW
bright = Style.BRIGHT
reset = Style.RESET_ALL


# Play the round
def play_round():
    """Play a single round of Rock, Paper, Scissors."""
    # Choices available for the game
    game_choices = ['Rock', 'Paper', 'Scissors', 'R', 'P', 'S']
    user_input = input(
        f"\n{yellow}{bright}" + f" Player ".center(22, "-") + f"{reset}{cyan}\n Choose from the following: \n\'Rock\'🪨  (r) , \'Paper\'📃 (p) , \'Scissors\'✂️  (s){reset}   ['q' to Quit]\n\n{blue} ---> {reset}").strip().title()
    print()

    if user_input in ['Q']:
        return "Q", None, None

    if user_input not in game_choices:
        return None, None, None

    if user_input in ['R', 'Rock']:
        user_choice = "Rock"
    elif user_input in ['P', 'Paper']:
        user_choice = "Paper"
    elif user_input in ['S', 'Scissors']:
        user_choice = "Scissors"

    # Define which choice beats which
    beats = {
        'Rock': 'Scissors',
        'Paper': 'Rock',
        'Scissors': 'Paper'
    }

    # Random choice by computer
    computer_choice = choice(["Rock", "Paper", "Scissors"])
    print(f"{green}Player's  choice : {magenta}{user_choice}\n{green}Computer's choice: {magenta}{computer_choice}")

    if computer_choice == user_choice:
        sleep(0.5)
        print(f"\n{bright}{magenta}||| It's a Draw ||| 😕{reset}")
        return 0, 0, 1
    else:
        if beats[user_choice] == computer_choice:
            print(f"\n{red}   {user_choice} ----→ {computer_choice}{reset}")
            sleep(0.5)
            print(f"{bright}{blue}\n!!! You Win !!! 😁{reset}")
            return 1, 0, 0
        else:
            print(f"\n{red}   {computer_choice} ----→ {user_choice}{reset}")
            sleep(0.5)
            print(f"{bright}{yellow}\n||| You Lose ||| 😭\nBetter Luck Next time{reset}")
            return 0, 1, 0

# Display the scoreboard
def display_scoreboard(player_score, computer_score, draw_count):
    """
    Display the final scoreboard.

    Prints the final scores of the player, the computer,
    and the number of draws in a neatly formatted table.

    Parameters:
    player_score (int): The score representing the number of rounds won by the player.
    computer_score (int): The score representing the number of rounds won by the computer.
    draw_count (int): The count of rounds that ended in a draw.
    """
    # Print the final scoreboard
    print(f"{cyan}{bright}----------------------------------")
    print("|      S C O R E  B O A R D      |")
    print("----------------------------------")
    print(f"|  {magenta}Player{cyan}  |  {yellow}Computer{cyan}  |  {green}Draw{cyan}  |")
    print("----------------------------------")
    print(f"|{magenta}{str(player_score).center(10)}{cyan}|{yellow}{str(computer_score).center(12)}{cyan}|{green}{str(draw_count).center(8)}{cyan}|")
    print(f"----------------------------------{reset}")


def main():
    """Main function to run the Rock, Paper, Scissors game."""
    print(f"\n{magenta}{bright}" + f" ROCK - PAPER - SCISSORS ".center(50, "*"))
    print(f"{magenta}{bright}" + f" NEW GAME ".center(50, "*"))
    player_score, computer_score, draw_count = 0, 0, 0

    while True:
        player_win, computer_win, draw = play_round()
        if player_win is None:
            print(f"{red}Invalid Input!\n{blue}Please enter \"Rock\"(r), \"Paper\"(p), or \"Scissors\"(s){reset}")
            sleep(1)
            print()
            continue
        elif player_win in ['Q']:
            print(f"{magenta}!!! Game Over !!!\nHOPE YOU ENJOYED 😇{reset}\n")
            sleep(0.5)
            display_scoreboard(player_score, computer_score, draw_count)
            break

        player_score += player_win
        computer_score += computer_win
        draw_count += draw

        sleep(0.5)
        play_again = input(f"{blue}\nDo you want to play again (y/n) [default: y]: ").strip().lower()
        if play_again in ["", "y", "yes"]:
            print()
            continue
        elif play_again in ["n", "no"]:
            sleep(0.5)
            print(f"\n{magenta}!!! Game Over !!!\nHOPE YOU ENJOYED 😇{reset}\n")
            sleep(0.5)
            display_scoreboard(player_score, computer_score, draw_count)
            break
        else:
            sleep(0.5)
            print(f"\n{red}Unrecognized Input\n{magenta}!!! Game Over !!!{reset}\n")
            sleep(0.5)
            display_scoreboard(player_score, computer_score, draw_count)
            break

if __name__ == '__main__':
    main()
