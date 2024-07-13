# Script: calculator.py
# Description: Simple Calculator with basic Arithmetic Operations.
# Author: Mohammed Abdul Raqeeb
# Date: 20/06/2024

try:
    from colorama import Fore, Style
except ImportError:
    print("\nERROR!\nThis script requires the 'colorama' module.\nPlease install it using 'pip install colorama' and try again.")
    exit(1)
from time import sleep


# Color settings
cyan = Fore.CYAN
green = Fore.GREEN
blue = Fore.BLUE
red = Fore.RED
yellow = Fore.YELLOW
bright = Style.BRIGHT
reset = Style.RESET_ALL


def calculator():
    """Displays the calculator menu and processes user input."""
    
    print(f'{yellow}{bright}\n' + f' SIMPLE CALCULATOR '.center(40, "-") + f'{reset}\n')

    user_input = input(
        f'{cyan}1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit' + f'{blue}{bright}\n\n----> {reset}')
    
    if user_input == '1':
        perform_calculation('Addition', '+')
    elif user_input == '2':
        perform_calculation('Subtraction', '-')
    elif user_input == '3':
        perform_calculation('Multiplication', '*')
    elif user_input == '4':
        perform_calculation('Division', '/')
    elif user_input == '5':
        print(f"{green}{bright}\nExiting...\nHave a nice day!{reset}")
        exit(0)
    else:
        sleep(0.2)
        print(f"{red}{bright}\nUnrecognized Input!!!{reset}")


def perform_calculation(operation, operator):
    """Performs the specified arithmetic operation."""
    
    print(f"{yellow}{bright}\n------ {operation} ------{reset}\n")
    try:
        first_operand = float(input('Enter first number: '))
        second_operand = float(input('Enter second number: '))
        
        result = f'{first_operand} {operator} {second_operand}'
        
        if first_operand.is_integer() and second_operand.is_integer() and operator != '/':
            print(f"\n{green}Result:\n{yellow}{int(first_operand)} {operator} {int(second_operand)} = {bright}{cyan}{int(eval(result))} {reset}")
        else:
            print(f"\n{green}Result:\n{yellow}{first_operand} {operator} {second_operand} = {bright}{cyan}%.2f {reset}" %eval(result))
            
    except ZeroDivisionError:
        print(f'\n{bright}{red}Cannot divide by zero!!!{reset}')
    except ValueError:
        print(f"\n{red}Invalid Input!\nPlease enter valid numeric value.{reset}")


def main():
    while True:
        calculator()
        sleep(0.5)
        user_input = input(f'{blue}\n\nDo you want to continue with further operations? (y/n) [default: y]: {reset}').lower()

        if user_input in ['', 'y', 'yes']:
            continue
        elif user_input in ['n', 'no']:
            print(f"{green}{bright}\nExiting...\nHave a nice day!{reset}")
            break
        else:
            print(f"{red}\nUnrecognized Input!!!\n\nExiting...\nHave a nice day!{reset}")
            break

if __name__ == '__main__':
    main()
