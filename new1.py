from math import hypot, sin, cos, tan, log, sqrt                 # My first ever program, created in python!
import time
import os
import colorama
cyan = colorama.Fore.CYAN
green = colorama.Fore.GREEN
black = colorama.Fore.BLACK
blue = colorama.Fore.BLUE
red = colorama.Fore.RED
yellow = colorama.Fore.YELLOW
light_green = colorama.Fore.LIGHTGREEN_EX
light_cyan = colorama.Fore.LIGHTCYAN_EX
finish = colorama.Style.RESET_ALL
os.system('clear')
print('Choose between the following: ')

def maths():
    try:
        user_input = (input(
            f'{light_cyan}Which Calculation do you want to make?:\n    Hypotenuse, Circumference, Square Root, Kinetic energy,'
            'Cube Root, Addition, Multiplication, Molecular weight,\n    Heat engine(Efficiency),'
            f' Sin, Cos, Tan, Log, notdefined-, exponent, Division.{finish}' + f'{blue}\n----> {finish}'))
    except:
        os.system('clear')
        exit()

    if user_input == "Hypotenuse" or user_input == "hypo":
        print('\nInput the lengths of the shorter triangle sides:')
        a = float(input('A: '))
        b = float(input('B: '))
        c = hypot(a, b)
        print("The length of the Hypotenuse is: %.2f" % c)

    elif user_input == "circumference" or user_input == "Circumference":
        Pi = 3.14
        r = float(input('Enter the radius of the circle: '))
        Area = Pi * r * r
        print('Circumference of the circle is Defined by: %.1f' % Area)

    elif user_input == "sqrt" or user_input == "Square Root":
        print('Input the number you want the Square root of: ')
        num1 = float(input('\nA: '))
        num = sqrt(num1)
        print('The Square Root of the given number is: %.3f' % num)

    elif user_input == "cbrt" or user_input == "Cube Root":
        print('Input the number you want the cube root of: ')
        x = float(input("\nA: "))
        y = x ** (1. / 3)
        print("The Cube Root of the Desired number is: %.2f" % y)

    elif user_input == "addition" or user_input == "Addition":
        print('Input the numbers which you want the sum of: ')
        p = float(input('\na: '))
        q = float(input('b: '))
        r = (p + q)
        print('The Sum of the Given numbers is: %.0f' % r)

    elif user_input == "Subtraction" or user_input == "minus":
        print('Enter the Values you want the differnce of: ')
        e = float(input('\na: '))
        f = float(input('b: '))
        g = (e - f)
        print('The Difference between the given numbers is: %.2f' % g)

    elif user_input == "multiplication" or user_input == "into":
        print('Enter the numbers you want the product of:')
        j = float(input('\na: '))
        k = float(input('b: '))
        i = (j * k)
        print('The product of the numbers is: %.2f' % i)

    elif user_input == "divide" or user_input == "Division":
        try:
            x = float(input('A: '))
            y = float(input('B: '))
            z = (x / y)
            print('The division is: %.2f' % z)
        except ZeroDivisionError:
            print('\nYou fool!\nCant divide by zero')

    elif user_input == "kinetic energy":
        print('What is the mass and velocity of the particle?')
        q = float(input('\nMass: '))
        w = float(input('Velocity: '))
        s = (1 / 2 * q * w * w)
        print('The Kinetic energy resolved is: %.1f' % s)

    elif user_input == "notdefined":
        try:
            num = int(input('State any number: '))
            init1 = int(input('State a given number: '))
            init2 = int(input('State another given number: '))
            x = 0
            for elements in range(num):
                if elements % init1 == 0 or elements % init2 == 0:
                    x += elements
            print(x)
        except:
            print('\nYou caused an error, dammit!\n')

    elif user_input == "Molecular weight" or user_input == "moleweight":
        print('Please provide the molecule details...: ')
        f = float(input('\nNumber of Carbon atoms: '))
        g = float(input('Number of Hydrogen atoms: '))
        h = ((f * 12.01) + (g * 1.01))
        print("The molecular weight is: %.3f" % h)

    elif user_input == "heat engine":
        print('Write down the temperatures: ')
        t1 = float(input('\nT1: '))
        t2 = float(input('T2: '))
        t = (1 - (t1 / t2))
        print('\nThe efficiency of the heat engine is: %.2f' % t)

    elif user_input == "sin":
        print('\nWhat is the angle of sine:\n')
        x = float(input())
        y = sin(x)
        print(y)

    elif user_input == "cos":
        print('\nWhat is the angle of cosecant? \n')
        x = float(input())
        y = cos(x)
        print(y)

    elif user_input == "tan":
        print('\nWhat is the angle of tan? \n')
        print('\nWhats the angle of tan? \n')
        x = float(input())
        y = tan(x)
        print(y)

    elif user_input == "log":
        x = float(input('\n    x : '))
        y = float(input('    Base: '))
        z = log(x, 7)
        print("The Logarithmic form is: %.2f" % z)

    elif user_input == "exponent":
        iterations = int(input("How many iterations? = "))  # asks the user how long does he wants the list to be
        times = range(iterations)
        create_alist = []  # an empty list where each answer is added
        for i in times:  # a for loop for iterations
            number = float(input("Enter the number :  "))
            power = float(input("Enter the power : "))
            answers = number ** power
            time.sleep(0.25)  # just for show
            print(answers)
            create_alist.append(answers)
        for i in create_alist:
            print(f"[{i}]")  # finally, the answers are printed line by line

    elif user_input == "exit":
        exit()

    else:
        time.sleep(0.2)
        os.system("clear")
        print(f"{red}Unrecognized Input!{finish}")


def loop_function():
    while True:
        maths()
        user_input = str(input(f'{blue}Do you want to continue? (Y/N){finish}'))
        os.system("clear")
        if user_input == "Y" or user_input == "y":
            continue
        elif user_input == "N" or user_input == "n":
            print(f"{red}Breaking...\nHave a nice day!{finish}")
            break

loop_function()
###