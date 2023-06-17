from math import hypot, sin, cos, tan, log, sqrt                  # My first ever program, created in python!
import time
import os
import platform
from colorama import Fore, Style

cyan, light_cyan = Fore.CYAN, Fore.LIGHTCYAN_EX
green, light_green = Fore.GREEN, Fore.LIGHTGREEN_EX
blue = Fore.BLUE
red = Fore.RED
yellow = Fore.YELLOW
dim, bright = Style.DIM, Style.BRIGHT
reset = Style.RESET_ALL


my_os = platform.system()
if my_os == "Windows":
    clear_Command = 'cls'
    os.system(clear_Command)
elif my_os == "Linux" or "Darwin":
    clear_Command = 'clear'
    os.system(clear_Command)    


def calcultor(): 

    print(f'{yellow}{bright}Choose between the following: {reset}\n')

    user_input = input(
        f'{cyan}1. Molecular weight\t\t2. Kinetic energy\t\t3. Heat engine(Efficiency)\n4. Hypotenuse'
        '\t\t\t5. Circumference\t\t6. Square Root\n7. Cube Root\t\t\t8. Logarithm\t\t\t9. Exponent\n10. Addition'
        f'\t\t\t11. Subtraction\t\t\t12. Multiplication\n13. Division\t\t\t14. Sin\t\t\t\t15. Cos\n16. Tan\t\t\t\t17. Notdefined\t\t\t18. Exit{reset}' + f'{blue}{bright}\n\n----> {reset}')
    
    if user_input == '1':
        print(f"{yellow}{bright}------ Molecular weight ------{reset}\n")
        print('Please provide the molecule details...:\n')
        try:
            f = int(input('Number of Carbon atoms: '))
            g = int(input('Number of Hydrogen atoms: '))
            h = ((f * 12.01) + (g * 1.01))
            print(f"\nThe Molecular Weight is:{bright}{light_cyan} %.3f" % h, end=f"{reset}")
        except ValueError:
            print("\nCarbon and Hydrogen atoms should be a Positive Integer value")         

    elif user_input == '2':
        print(f"{yellow}{bright}------ Kinetic energy ------{reset}\n")
        print('What is the mass and velocity of the particle?\n')
        try:
            q = float(input('Mass: '))
            w = float(input('Velocity: '))
            s = (1 / 2 * q * w * w)
            print(f'\nThe Kinetic energy resolved is:{bright}{light_cyan} %.1f' % s, end=f"{reset}")
        except ValueError:
            print("Mass and Velocity should be a Positive Number")

    elif user_input == '3':
        print(f"{yellow}{bright}------ Heat engine(Efficiency) ------{reset}\n")
        print('Write down the Temperatures: \n')
        try:
            t1 = float(input('T1: '))
            t2 = float(input('T2: '))
            t = (1 - (t1 / t2))
            print(f'\nThe Efficiency of the heat engine is:{bright}{light_cyan} %.2f' % t, end=f"{reset}")
        except ValueError:
            print("Invalid Temperature")

    elif user_input == '4':
        print(f"{yellow}{bright}------ Hypotenuse ------{reset}\n")
        print('Input the Lengths of the shorter Triangle sides:\n')
        try:
            a = float(input('A: '))
            b = float(input('B: '))
            c = hypot(a, b)
            print(f"\nThe Length of the Hypotenuse is:{bright}{light_cyan} %.2f" % c, end=f"{reset}")
        except ValueError:
            print("Enter Positive Length of Triangle side")            

    elif user_input == '5':
        print(f"{yellow}{bright}------ Circumference ------{reset}\n")
        Pi = 3.14
        try:
            r = float(input('Enter the radius of the circle: '))
            Area = Pi * r * r
            print(f'\nCircumference of the circle is Defined by:{bright}{light_cyan} %.1f' % Area, end=f"{reset}")
        except ValueError:
            print("Enter Positive Radius of Circle")

    elif user_input == '6':
        print(f"{yellow}{bright}------ Square Root ------{reset}\n")
        try:
            num1 = float(input('Input the number you want the Square root of: '))
            num = sqrt(num1)
            print(f'\nThe Square Root of the given number is:{bright}{light_cyan} %.3f' % num, end=f"{reset}")
        except ValueError:
            print("Enter Positive Number")

    elif user_input == '7':
        print(f"{yellow}{bright}------ Cube Root ------{reset}\n")
        try:
            x = float(input("Input the number you want the cube root of: "))
            y = x ** (1 / 3)
            print(f"\nThe Cube Root of the Desired number is:{bright}{light_cyan} %.2f" % y, end=f"{reset}")
        except ValueError:
            print("Enter Positive Number")

    elif user_input == '8':
        print(f"{yellow}{bright}------ Logarithm ------{reset}\n")
        try:
            x = float(input('x : '))
            y = float(input('Base: '))
            z = log(x, y)
            print(f"The Logarithmic form is:{bright}{light_cyan} %.2f" % z, end=f"{reset}")
        except ValueError:
            print("Enter Positive Number")

    elif user_input == '9':
        print(f"{yellow}{bright}------ Exponent ------{reset}\n")
        try:
            iterations = int(input("How many iterations? = "))       # asks the user how long does he wants the list to be
            times = range(iterations)
            create_alist = []                     # an empty list where each answer is added
            for i in times:                # a for loop for iterations
                number = float(input("Enter the number :  "))
                power = float(input("Enter the power : "))
                answers = number ** power
                time.sleep(0.25)          # just for show
                print("The Result is :", answers, "\n")
                create_alist.append(answers)
            for i in create_alist:
                print(f"{bright}{light_cyan}[{i}]", end=f"{reset} ")         # finally, the answers are printed line by line
            print()
        except ValueError:
            print("Enter Positive Number")

    elif user_input == '10':
        print(f"{yellow}{bright}------ Addition ------{reset}\n")
        print('Input the numbers which you want the sum of: \n')
        try:
            p = float(input('A: '))
            q = float(input('B: '))
            r = (p + q)
            print(f'\nThe Sum of the Given numbers is:{bright}{light_cyan} %.0f' % r, end=f"{reset}")
        except ValueError:
            print("Invalid Input")

    elif user_input == '11':
        print(f"{yellow}{bright}------ Subtraction ------{reset}\n")
        print('Enter the Values you want the differnce of: \n')
        try:
            e = float(input('A: '))
            f = float(input('B: '))
            g = (e - f)
            print(f'\nThe Difference between the given numbers is:{bright}{light_cyan} %.2f' % g, end=f"{reset}")
        except ValueError:
            print("Invalid Input")

    elif user_input == '12':
        print(f"{yellow}{bright}------ Multiplication ------{reset}\n")
        print('Enter the numbers you want the product of:\n')
        try:
            j = float(input('A: '))
            k = float(input('B: '))
            i = (j * k)
            print(f'\nThe product of the numbers is:{bright}{light_cyan} %.2f' % i, end=f"{reset}")
        except ValueError:
            print("Invalid Input")

    elif user_input == '13':
        print(f"{yellow}{bright}------ Division ------{reset}\n")
        try:
            try:
                x = float(input('Enter the numbers you want to divide:\n\nA: '))
                y = float(input('B: '))
                z = (x / y)
                print(f'\nThe division is:{bright}{light_cyan} %.2f' % z, end=f"{reset}")
            except ValueError:
                print("Invalid Input")
        except ZeroDivisionError:
            print(f'\n{bright}{cyan}You fool!\nCant divide by zero', end=f"{reset}")

    elif user_input == '14':
        print(f"{yellow}{bright}------ Sin------{reset}\n")
        print('What is the angle of Sine? \n')
        try:
            x = float(input("θ° = "))
            y = sin(x)
            print(f"\nThe value of{bright}{light_cyan} Sin", int(x), "=", y, end=f"{reset}")
        except ValueError:
            print("Invalid Input. Enter Sine angle correctly")

    elif user_input == '15':
        print(f"{yellow}{bright}------ Cos ------{reset}\n")
        print('What is the angle of CoSecant? ')
        try:
            x = float(input("θ° = "))
            y = cos(x)
            print(f"\nThe value of{bright}{light_cyan} Cos", int(x), "=", y, end=f"{reset}\n")
        except ValueError:
            print("Invalid Input. Enter Cos angle correctly")

    elif user_input == '16':
        print(f"{yellow}{bright}------ Tan ------{reset}\n")
        print('Whats the angle of tan? \n')
        try:
            x = float(input("θ° = "))
            y = tan(x)
            print(f"\nThe value of{bright}{light_cyan} Tan", int(x), "=", y, end=f"{reset}")
        except ValueError:
            print("Invalid Input. Enter Tan angle correctly")

    elif user_input == '17':
        print(f"{yellow}{bright}------ Notdefined ------{reset}\n")
        try:
            try:
                num = int(input('State any number: '))
                init1 = int(input('State a given number: '))
                init2 = int(input('State another given number: '))
                x = 0
                for elements in range(num):
                    if elements % init1 == 0 or elements % init2 == 0:
                        x += elements
                print(f"{bright}{light_cyan}\nResult = ", x, end=f"{reset}")
            except ValueError:
                print("Enter Integer Value")
        except:
            print('\nYou caused an error, dammit!\n')

    elif user_input == '18':
        print(f"{bright}{yellow}!!!THANK YOU!!!{reset}")
        exit()

    else:
        time.sleep(0.2)
        print(f"{red}{bright}Unrecognized Input!!!{reset}")


def loop_function():
    while True:
        calcultor()
        time.sleep(0.5)
        user_input = input(f'{blue}\n\nDo you want to continue with further operations? (Y/N): {reset}').upper()

        if user_input == "Y" or user_input == "YES":
            os.system(clear_Command)
            continue
        elif user_input == "N" or user_input == "NO" :
            print(f"{red}Breaking...\nHave a nice day!{reset}")
            break
        else:
            print(f"{red}Unrecognized Input!!!{dim}\n\nBreaking...\nHave a nice day!{reset}")
            break

loop_function()
###