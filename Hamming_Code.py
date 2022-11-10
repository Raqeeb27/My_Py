from colorama import Fore as f, Style as s
from time import sleep

yellow, lyellow = f.YELLOW, f.LIGHTYELLOW_EX
red, lred = f.RED, f.LIGHTRED_EX
blue, lblue = f.BLUE, f.LIGHTBLUE_EX
lcyan = f.LIGHTCYAN_EX
dim, bright = s.DIM, s.BRIGHT
reset, normal = s.RESET_ALL, s.NORMAL

def parity_correct(i,error):
    print(f"{red}{dim}There is an Error in Parity Bit \'P{i}\'{reset}")
    if parity_bits[f"P{i}"] == "0":
        parity_bits[f"P{i}"] = "1"
        error = 1
    elif parity_bits[f"P{i}"] == "1":
        parity_bits[f"P{i}"] = "0"
        error = 1
    return error

orig_frame = input(
    f"{lyellow}{bright}\n----ERROR DETECTION AND ERROR CORRECTION----{normal}\n\n{dim}{lcyan}Enter the Hamming Code Frame (with greater than 7 digits):{reset} ")
orig_frame = orig_frame[::-1]

if orig_frame.count("1") + orig_frame.count("0") != len(orig_frame):
    print(f"\n{lred}-----INVALID INPUT-----\n\n{blue}Frame has only Binary Digits {bright}\'0\' & \'1\'{reset}")
    exit()
if len(orig_frame) < 8 or len(orig_frame) > 16:
    print(f"\n{lred}{dim}Enter number of Digits between 8 t0 15{reset}")
    exit()

parity_bits = {"P1": str(orig_frame[2 ** 0 - 1]), "P2": str(orig_frame[2 ** 1 - 1]), "P4": str(orig_frame[2 ** 2 - 1]),
               "P8": str(orig_frame[2 ** 3 - 1])}

print("\nParity bits are: ", parity_bits)
for i in range(len(orig_frame)):
    if 2 ** i >= len(orig_frame) + 1 + i:
        if i == 5:
            print("Total Parity Bits are 4")
            break
        else:
            print("Total Parity Bits are:", i)
            break

sleep(0.4)
eve_odd = input(f"{yellow}\nUsing ODD Parity or EVEN Parity(O/E): {reset}")
print()
error = 0
for i in range(1, 5):
    frame = []
    if i == 1:
        frame = [x for x in orig_frame[0:len(orig_frame):2]]
    elif i == 2:
        for i in range(len(orig_frame)):
            if i == 0 or i == 3 or i == 4 or i == 7 or i == 8 or i == 11 or i == 12 or i == 15:
                continue
            frame.append(orig_frame[i])
        i = 2
    elif i == 3:
        for i in range(len(orig_frame)):
            if i == 0 or i == 1 or i == 2 or i == 7 or i == 8 or i == 9 or i == 10 or i == 15:
                continue
            frame.append(orig_frame[i])
        i = 4
    elif i == 4:
        for i in range(len(orig_frame)):
            if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 15:
                continue
            frame.append(orig_frame[i])
        i = 8
    frame = "".join(frame)
    if eve_odd == "o" or eve_odd == "O" or eve_odd == "0" or eve_odd == "odd" or eve_odd == "ODD" or eve_odd == "Odd":
        if frame.count("1") % 2 == 0:
            error = parity_correct(i,0)
    elif eve_odd == "e" or eve_odd == "E" or eve_odd == "EVEN" or eve_odd == "Even" or eve_odd == "even":
        if frame.count("1") % 2 != 0:
            error = parity_correct(i,0)
    else:
        print(f"{lred}Invalid Input\nTry again{reset}")
        exit()

sleep(0.4)
if error == 0:
    print(
        f"{bright}{lcyan}The entered Frame ---{orig_frame}--- has no error with the given parity \'{eve_odd}\'{reset}")
    exit()

print(f"\n{lblue}Corrected Parity Bits: {parity_bits}{reset}")
orig_frame = [x for x in orig_frame]
orig_frame[0] = parity_bits["P1"]
orig_frame[1] = parity_bits["P2"]
orig_frame[3] = parity_bits["P4"]
orig_frame[7] = parity_bits["P8"]
orig_frame = "".join(orig_frame)
sleep(0.4)
print(f"\n{bright}{lcyan}Corrected Frame: ---{orig_frame[::-1]}---{reset}")
