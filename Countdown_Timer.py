import sys
from time import sleep
from colorama import Fore, Style
from pyfiglet import figlet_format


CYAN, LIGHT_CYAN = Fore.CYAN, Fore.LIGHTCYAN_EX
GREEN, LIGHT_GREEN = Fore.GREEN, Fore.LIGHTGREEN_EX
BLUE = Fore.BLUE
RED = Fore.RED
YELLOW = Fore.YELLOW
DIM, BRIGHT = Style.DIM, Style.BRIGHT
RESET = Style.RESET_ALL


def countdown(timer):
    print(f"{YELLOW}")
    last_lines = 0
    while timer >= 0:
        hours, remainder = divmod(timer, 3600)
        minutes, seconds = divmod(remainder, 60)
        display_time = f'{hours:02d} : {minutes:02d} : {seconds:02d}'

        # Render figlet text
        big_text = figlet_format(display_time, font="big")
        lines = big_text.splitlines()

        # Move cursor up to overwrite previous lines
        if last_lines:
            sys.stdout.write("\033[F" * last_lines)

        # Print and flush
        for line in lines:
            sys.stdout.write("\033[K" + line + "\n")
        sys.stdout.flush()

        last_lines = len(lines)
        timer -= 1
        if timer < 0:
            return
        sleep(1)


print(f"\n{BRIGHT}{YELLOW} " + " Countdown ".center(19, "-")+ f"")

try:
    input_time = int(input(f"\n{LIGHT_CYAN}Enter the time in seconds: "))
    if input_time <= 0:
        print(f"\n{RED}Invalid input!\n{BLUE}Please enter a positive integer.\n")
        sys.exit(1)
except ValueError:
    print(f"\n{RED}Invalid input!\n{BLUE}Please enter a positive integer.\n")
    sys.exit(1)
except (KeyboardInterrupt, EOFError):
    print(f"\n\n{RED}Keyboard Interrupt!!!\n{BLUE}Exiting...\n")
    sys.exit(1)

try:
    input(f"\n{BLUE} --> Press Enter to start the timer when ready: ")
    countdown(input_time)
except (KeyboardInterrupt, EOFError):
    print(f"\n\n{RED}Keyboard Interrupt!!!\n{BLUE}Exiting...\n")
    sys.exit(1)
except Exception as e:
    print(f"\n\n{RED}Error: {e}")
    sys.exit(1)

print(f"{CYAN}  !!! Times Up !!!{RESET}\n")
