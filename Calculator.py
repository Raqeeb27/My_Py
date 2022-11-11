from math import hypot, sin, cos, tan, log, sqrt  # My first ever program, created in python!
import time
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
dim = colorama.Style.DIM
bright = colorama.Style.BRIGHT

print(f'{yellow}Choose between the following: {finish}\n')


def maths():
    try:
        user_input = (input(
            f'{cyan}{dim}Which Calculation do you want to make?:\n1.Molecular weight\t\t2.Kinetic energy\t\t3.Heat engine(Efficiency)\n4.Hypotenuse'
            '\t\t\t5.Circumference\t\t\t6.Square Root\n7.Cube Root\t\t\t\t8.Log\t\t\t\t\t9.Exponent\n10.Addition'
            f'\t\t\t\t11.Subtraction\t\t\t12.Multiplication\n13.Division\t\t\t\t14.Sin\t\t\t\t\t15.Cos\n16.Tan\t\t\t\t\t17.Notdefined\t\t\t18.Exit{finish}' + f'{blue}{bright}\n----> {finish}'))
    except:
        exit()

    if user_input == '1':
        print('Please provide the molecule details...: ')
        f = float(input('\nNumber of Carbon atoms: '))
        g = float(input('Number of Hydrogen atoms: '))
        h = ((f * 12.01) + (g * 1.01))
        print(f"\nThe Molecular Weight is:{bright}{light_cyan} %.3f" % h, end=f"{finish}")

    elif user_input == '2':
        print('What is the mass and velocity of the particle?')
        q = float(input('\nMass: '))
        w = float(input('Velocity: '))
        s = (1 / 2 * q * w * w)
        print(f'\nThe Kinetic energy resolved is:{bright}{light_cyan} %.1f' % s, end=f"{finish}")

    elif user_input == '3':
        print('Write down the Temperatures: ')
        t1 = float(input('\nT1: '))
        t2 = float(input('T2: '))
        t = (1 - (t1 / t2))
        print(f'\nThe Efficiency of the heat engine is:{bright}{light_cyan} %.2f' % t, end=f"{finish}")

    elif user_input == '4':
        print('\nInput the lengths of the shorter triangle sides:\n')
        a = float(input('A: '))
        b = float(input('B: '))
        c = hypot(a, b)
        print(f"\nThe Length of the Hypotenuse is:{bright}{light_cyan} %.2f" % c, end=f"{finish}")

    elif user_input == '5':
        Pi = 3.14
        r = float(input('Enter the radius of the circle: '))
        Area = Pi * r * r
        print(f'\nCircumference of the circle is Defined by:{bright}{light_cyan} %.1f' % Area, end=f"{finish}")


    elif user_input == '6':
        num1 = float(input('Input the number you want the Square root of: '))
        num = sqrt(num1)
        print(f'\nThe Square Root of the given number is:{bright}{light_cyan} %.3f' % num, end=f"{finish}")

    elif user_input == '7':
        x = float(input("Input the number you want the cube root of: "))
        y = x ** (1 / 3)
        print(f"\nThe Cube Root of the Desired number is:{bright}{light_cyan} %.2f" % y, end=f"{finish}")

    elif user_input == '8':
        x = float(input('---Logarithmic calculator---\n\tx : '))
        y = float(input('\tBase: '))
        z = log(x, y)
        print(f"The Logarithmic form is:{bright}{light_cyan} %.2f" % z, end=f"{finish}")

    elif user_input == '9':
        iterations = int(input("How many iterations? = "))  # asks the user how long does he wants the list to be
        times = range(iterations)
        create_alist = []  # an empty list where each answer is added
        for i in times:  # a for loop for iterations
            number = float(input("Enter the number :  "))
            power = float(input("Enter the power : "))
            answers = number ** power
            time.sleep(0.25)  # just for show
            print("The Result is :", answers, "\n")
            create_alist.append(answers)
        for i in create_alist:
            print(f"{bright}{light_cyan}[{i}]", end=f"{finish} ")  # finally, the answers are printed line by line
        print()

    elif user_input == '10':
        print('Input the numbers which you want the sum of: ')
        p = float(input('\nA: '))
        q = float(input('B: '))
        r = (p + q)
        print(f'\nThe Sum of the Given numbers is:{bright}{light_cyan} %.0f' % r, end=f"{finish}")

    elif user_input == '11':
        print('Enter the Values you want the differnce of: ')
        e = float(input('\nA: '))
        f = float(input('B: '))
        g = (e - f)
        print(f'\nThe Difference between the given numbers is:{bright}{light_cyan} %.2f' % g, end=f"{finish}")

    elif user_input == '12':
        print('Enter the numbers you want the product of:')
        j = float(input('\nA: '))
        k = float(input('B: '))
        i = (j * k)
        print(f'\nThe product of the numbers is:{bright}{light_cyan} %.2f' % i, end=f"{finish}")

    elif user_input == '13':
        try:
            x = float(input('Enter the numbers you want to divide:\nA: '))
            y = float(input('B: '))
            z = (x / y)
            print(f'\nThe division is:{bright}{light_cyan} %.2f' % z, end=f"{finish}")
        except ZeroDivisionError:
            print(f'\n{bright}You fool!\nCant divide by zero', end=f"{finish}")

    elif user_input == '14':
        print('\nWhat is the angle of sine? \n')
        x = float(input("θ° = "))
        y = sin(x)
        print(f"\nThe value of{bright}{light_cyan} Sin", int(x), "=", y, end=f"{finish}")

    elif user_input == '15':
        print('\nWhat is the angle of cosecant? ')
        x = float(input("θ° = "))
        y = cos(x)
        print(f"\nThe value of{bright}{light_cyan} Cos", int(x), "=", y, end=f"{finish}\n")

    elif user_input == '16':
        print('\nWhats the angle of tan? \n')
        x = float(input("θ° = "))
        y = tan(x)
        print(f"\nThe value of{bright}{light_cyan} Tan", int(x), "=", y, end=f"{finish}")

    elif user_input == '17':
        try:
            num = int(input('State any number: '))
            init1 = int(input('State a given number: '))
            init2 = int(input('State another given number: '))
            x = 0
            for elements in range(num):
                if elements % init1 == 0 or elements % init2 == 0:
                    x += elements
            print(f"{bright}{light_cyan}Result = ", x, end=f"{finish}")
        except:
            print('\nYou caused an error, dammit!\n')

    elif user_input == '18':
        print("!!!THANK YOU!!!")
        exit()

    else:
        time.sleep(0.2)
        print(f"{red}{dim}Unrecognized Input!{finish}")


def loop_function():
    while True:
        maths()
        time.sleep(0.2)
        user_input = input(f'{blue}{dim}\n\nDo you want to continue with further operations? (Y/N): {finish}').title()

        if user_input == "Y" or user_input == "YES" or user_input == "Yes":
            print()
            continue
        elif user_input == "NO" or user_input == "No" or user_input == "N" :
            print(f"{red}{dim}Breaking...\nHave a nice day!{finish}")
            break
        else:
            print(f"{red}{dim}Unrecognized Input!!!\n\nBreaking...\nHave a nice day!{finish}")
            break


loop_function()
###
