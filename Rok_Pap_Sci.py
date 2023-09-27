from random import choice
from time import sleep
from colorama import Fore as f, Style as s

lyellow, lcyan = f.LIGHTYELLOW_EX, f.LIGHTCYAN_EX
lred, lblue, magenta = f.LIGHTRED_EX, f.LIGHTBLUE_EX, f.MAGENTA
lgreen, lmagenta, white = f.LIGHTGREEN_EX, f.LIGHTMAGENTA_EX, f.WHITE
bright, dim, yellow = s.BRIGHT, s.DIM, f.YELLOW
reset = s.RESET_ALL

while True:
    user_input = input(
        f"{lyellow}{bright}-----Player-1-----{lcyan}\nChoose from the following: \n\'Rock\' (r) , \'Paper\' (p) , \'Scissors\' (s) ? :{bright} {reset}").title()
    print()

    if user_input == "R":
        user_input = "Rock"
    elif user_input == "P":
        user_input = "Paper"
    elif user_input == "S":
        user_input = "Scissors"

    ran_value = choice(["Rock", "Paper", "Scissors"])

    if user_input != "Rock" and user_input != "Scissors" and user_input != "Paper":
        print(f"{lred}-----Invalid Input-----\n\n{lblue}Please enter \"Rock\" ,\"Paper\" ,\"Scissor\"{reset}")

    elif ran_value == user_input:
        print(
            f"{lgreen}Player-1 selected: {lmagenta}{user_input}\n{lgreen}Player-2 selected: {lmagenta}{ran_value}\n\n{bright}{lyellow}|||It's a Draw||| 😕{reset}")

    else:
        if ran_value == "Rock":
            if user_input == "Paper":
                print(
                    f"{lgreen}Player-1 selected: {lmagenta}{user_input}\n{lgreen}Player-2 selected: {lmagenta}{ran_value}\n{lred}   Paper ----→ Rock{bright}{lblue}\n\n!!!You Win!!! 😁{reset}")
            else:
                print(
                    f"{lgreen}Player-1 selected: {lmagenta}{user_input}\n{lgreen}Player-2 selected: {lmagenta}{ran_value}\n{lred}   Rock ----→ Scissors{bright}{lyellow}\n\n|||You Lose|||{lred} 😭\nBetter Luck Next time{reset}")

        elif ran_value == "Paper":
            if user_input == "Scissors":
                print(
                    f"{lgreen}Player-1 selected: {lmagenta}{user_input}\n{lgreen}Player-2 selected: {lmagenta}{ran_value}\n{lred}   Scissors ----→ Paper{bright}{lblue}\n\n!!!You Win!!! 😁{reset}")
            else:
                print(
                    f"{lgreen}Player-1 selected: {lmagenta}{user_input}\n{lgreen}Player-2 selected: {lmagenta}{ran_value}\n{lred}   Paper ----→ Rock{bright}{lyellow}\n\n|||You Lose||| {lred}😭\nBetter Luck Next time{reset}")

        elif ran_value == "Scissors":
            if user_input == "Rock":
                print(
                    f"{lgreen}Player-1 selected: {lmagenta}{user_input}\n{lgreen}Player-2 selected: {lmagenta}{ran_value}\n{lred}   Rock ----→ Scissors{bright}{lblue}\n\n!!!You Win!!! 😁{reset}")
            else:
                print(
                    f"{lgreen}Player-1 selected: {lmagenta}{user_input}\n{lgreen}Player-2 selected: {lmagenta}{ran_value}\n{lred}   Scissors ----→ Paper{bright}{lyellow}\n\n|||You Lose|||{lred} 😭\nBetter Luck Next time{reset}")
    sleep(0.5)
    play = input(f"{yellow}{dim}\nDo you want to play again (Y/N): ").upper()
    if play in ["YES","Y"] :
        print()
        continue
    elif play in ["NO","N"]:
        print(f"{magenta}!!!Game Over!!!\nHOPE YOU Enjoyed😇{reset}\n")
        break
    else:
        print(f"{lred}Unrecognised Input\n!!!Game Over!!!{reset}\n")
        break
