# Script: password_generator.py
# Description: Tool that generates Strong and Random Passwords for Users.
# Author: Mohammed Abdul Raqeeb
# Date: 14/06/2024

try:
    from colorama import Fore, Style
except ImportError:
    print("This script requires the 'colorama' module.\nPlease install it using 'pip install colorama' and try again.")
    exit(1)

import string
from random import shuffle
from secrets import choice
from time import sleep


# Define character sets
LOWER_CHARS = string.ascii_lowercase
UPPER_CHARS = string.ascii_uppercase
DIGITS = string.digits
SPECIAL_CHARS = string.punctuation

# Define colorama attributes
cyan = Fore.CYAN
green = Fore.GREEN
blue = Fore.BLUE
red = Fore.RED
yellow = Fore.YELLOW
bright = Style.BRIGHT
reset = Style.RESET_ALL

# Function to generate password
def generate_password(password_length, use_lower=False, use_upper=False, use_digits=False, use_special=False):
    """
    Generates a strong random password of a specified length based on user preferences.

    Parameters:
    password_length (int): The length of the password to be generated.
    use_lower (bool): Include lowercase letters if True.
    use_upper (bool): Include uppercase letters if True.
    use_digits (bool): Include digits if True.
    use_special (bool): Include special characters if True.

    Returns:
    str: The generated password.
    """

    char_pool = ''
    password = []

    if use_lower:
        char_pool += LOWER_CHARS
        password.append(choice(LOWER_CHARS))
    if use_upper:
        char_pool += UPPER_CHARS
        password.append(choice(UPPER_CHARS))
    if use_digits:
        char_pool += DIGITS
        password.append(choice(DIGITS))
    if use_special:
        char_pool += SPECIAL_CHARS
        password.append(choice(SPECIAL_CHARS))

    if not char_pool:
        print(f"{red}\nNo character types selected for password generation.{reset}")
        exit(1)

    # Add random characters to fill the rest of the password length
    password += [choice(char_pool) for _ in range(password_length - len(password))]

    # Shuffle the password to ensure randomness
    for _ in range(3):
        shuffle(password)

    return ''.join(password)

def main():
    print(f"\n{yellow}{bright}" + " PASSWORD GENERATOR ".center(40, "-") + f"{reset}")
    sleep(0.75)

    try:
        password_length = int(input(f'\n{cyan}Enter the length of the password to be generated: {reset}').strip())

        if password_length < 4 or password_length > 256:
            print(f"\n{red}Password length must be between 4 and 256 characters.\nPlease try again.{reset}\n")
            exit(1)

        print(f"{yellow}\n\nSelect character types to include in the password:")
        use_lower = input(f'{green}\nInclude lowercase letters (y/n) {blue}[default: y]: {reset}').strip().lower() in ['','y','yes']
        use_upper = input(f'{green}Include uppercase letters (y/n) {blue}[default: y]: {reset}').strip().lower() in ['','y','yes']
        use_digits = input(f'{green}Include digits (y/n) {blue}[default: y]: {reset}').strip().lower() in ['','y','yes']
        use_special = input(f'{green}Include special characters (y/n) {blue}[default: y]: {reset}').strip().lower() in ['','y','yes']

        password = generate_password(password_length, use_lower, use_upper, use_digits, use_special)

        print(f'\n\n{green}Your Robust Generated Password is: \n{yellow}{bright}{password}{reset}\n')

    except ValueError:
        print(f"\n{red}Invalid input.\nPlease enter a valid integer for the password length.{reset}\n")
        exit(1)

if __name__ == '__main__':
    main()
