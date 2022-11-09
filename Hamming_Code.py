from colorama import Fore as f, Style as s
from time import sleep
yellow = f.YELLOW
dim = s.DIM
bright = s.BRIGHT
reset = s.RESET_ALL
lcyan = f.LIGHTCYAN_EX
normal = s.NORMAL
red = f.RED
lred = f.LIGHTRED_EX
blue = f.BLUE
lyellow = f.LIGHTYELLOW_EX
lblue = f.LIGHTBLUE_EX

def O_parity_bit_P1(a, b):
    frame = [x for x in a[0:len(a):2]]
    frame = "".join(frame)
    if frame.count("1") % 2 == 0:
        print(f"{red}{dim}There is an Error in Parity Bit \'P1\'{reset}")
        if parity_bits["P1"] == "0":
            parity_bits["P1"] = "1"
            return parity_bits
        elif parity_bits["P1"] == "1":
            parity_bits["P1"] = "0"
            return parity_bits

def E_parity_bit_P1(a, b):
    frame = [x for x in a[0:len(a):2]]
    frame = "".join(frame)
    if frame.count("1") % 2 != 0:
        print(f"{red}{dim}There is an Error in Parity Bit \'P1\'{reset}")
        if parity_bits["P1"] == "0":
            parity_bits["P1"] = "1"
            return parity_bits
        elif parity_bits["P1"] == "1":
            parity_bits["P1"] = "0"
            return parity_bits

def O_parity_bit_P2(a, b):
    frame = []
    for i in range(len(a)):
        if i == 0 or i == 3 or i == 4 or i == 7 or i == 8 or i == 11 or i == 12 or i == 15:
            continue
        frame.append(a[i])
    frame = "".join(frame)
    if frame.count("1") % 2 == 0:
        print(f"{red}{dim}There is an Error in Parity Bit \'P2\'{reset}")
        if parity_bits["P2"] == "0":
            parity_bits["P2"] = "1"
            return parity_bits
        elif parity_bits["P2"] == "1":
            parity_bits["P2"] = "0"
            return parity_bits

def E_parity_bit_P2(a, b):
    frame = []
    for i in range(len(a)):
        if i == 0 or i == 3 or i == 4 or i == 7 or i == 8 or i == 11 or i == 12 or i == 15:
            continue
        frame.append(a[i])
    frame = "".join(frame)
    if frame.count("1") % 2 != 0:
        print(f"{red}{dim}There is an Error in Parity Bit \'P2\'{reset}")
        if parity_bits["P2"] == "0":
            parity_bits["P2"] = "1"
            return parity_bits
        elif parity_bits["P2"] == "1":
            parity_bits["P2"] = "0"
            return parity_bits

def O_parity_bit_P3(a, b):
    frame = []
    for i in range(len(a)):
        if i == 0 or i == 1 or i == 2 or i == 7 or i == 8 or i == 9 or i == 10 or i == 15:
            continue
        frame.append(a[i])
    frame = "".join(frame)
    if frame.count("1") % 2 == 0:
        print(f"{red}{dim}There is an Error in Parity Bit \'P3\'{reset}")
        if parity_bits["P3"] == "0":
            parity_bits["P3"] = "1"
            return parity_bits
        elif parity_bits["P3"] == "1":
            parity_bits["P3"] = "0"
            return parity_bits

def E_parity_bit_P3(a, b):
    frame = []
    for i in range(len(a)):
        if i == 0 or i == 1 or i == 2 or i == 7 or i == 8 or i == 9 or i == 10 or i == 15:
            continue
        frame.append(a[i])
    frame = "".join(frame)
    if frame.count("1") % 2 != 0:
        print(f"{red}{dim}There is an Error in Parity Bit \'P3\'{reset}")
        if parity_bits["P3"] == "0":
            parity_bits["P3"] = "1"
            return parity_bits
        elif parity_bits["P3"] == "1":
            parity_bits["P3"] = "0"
            return parity_bits


def O_parity_bit_P4(a, b):
    frame = []
    for i in range(len(a)):
        if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 15:
            continue
        frame.append(a[i])
    frame = "".join(frame)
    if frame.count("1") % 2 == 0:
        print(f"{red}{dim}There is an Error in Parity Bit \'P4\'{reset}")
        if parity_bits["P4"] == "0":
            parity_bits["P4"] = "1"
            return parity_bits
        elif parity_bits["P4"] == "1":
            parity_bits["P4"] = "0"
            return parity_bits


def E_parity_bit_P4(a, b):
    frame = []
    for i in range(len(a)):
        if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 15:
            continue
        frame.append(a[i])
    frame = "".join(frame)
    if frame.count("1") % 2 != 0:
        print(f"{red}{dim}There is an Error in Parity Bit \'P4\'{reset}")
        if parity_bits["P4"] == "0":
            parity_bits["P4"] = "1"
            return parity_bits
        elif parity_bits["P4"] == "1":
            parity_bits["P4"] = "0"
            return parity_bits

orig_frame = input(f"{lyellow}{bright}\n----ERROR DETECTION AND ERROR CORRECTION----{normal}\n\n{dim}{lcyan}Enter the Hamming Code Frame (with greater than 7 digits):{reset} ")
orig_frame = orig_frame[::-1]

if orig_frame.count("1") + orig_frame.count("0") != len(orig_frame):
    print(f"\n{lred}-----INVALID INPUT-----\n\n{blue}Frame has only Binary Digits {bright}\'0\' & \'1\'{reset}")
    exit()

if len(orig_frame) < 8 or len(orig_frame) > 16:
    print(f"\n{lred}{dim}Enter number of Digits between 8 t0 15{reset}")
    exit()

parity_bits = {"P1":str(orig_frame[2 ** 0 - 1]) , "P2": str(orig_frame[2 ** 1 - 1]), "P3": str(orig_frame[2 ** 2 - 1]), "P4":str(orig_frame[2 ** 3 - 1])}
print("\nParity bits are: ",parity_bits)

for i in range(len(orig_frame)):
    if 2 ** i >= len(orig_frame) + 1 + i:
        if i == 5:
            print("Total Parity Bits are 4")
            break
        else:
            print("Total Parity Bits are", i)
            break
sleep(0.4)
eve_odd = input(f"{yellow}\nUsing ODD Parity or EVEN Parity(O/E): {reset}")
print()
if eve_odd == "o" or eve_odd == "O" or eve_odd == "0" or eve_odd == "odd" or eve_odd == "ODD" or eve_odd == "Odd":
    O_parity_bit_P1(orig_frame, parity_bits)
    O_parity_bit_P2(orig_frame, parity_bits)
    O_parity_bit_P3(orig_frame, parity_bits)
    O_parity_bit_P4(orig_frame, parity_bits)
elif eve_odd == "e" or eve_odd == "E" or eve_odd == "EVEN" or eve_odd == "Even" or eve_odd == "even":
    E_parity_bit_P1(orig_frame, parity_bits)
    E_parity_bit_P2(orig_frame, parity_bits)
    E_parity_bit_P3(orig_frame, parity_bits)
    E_parity_bit_P4(orig_frame, parity_bits)
else:
    print(f"{lred}Invalid Input\nTry again{reset}")
    exit()
sleep(0.4)

print(f"\n{lblue}Corrected Parity Bits: {parity_bits}{reset}")
orig_frame = [x for x in orig_frame]
orig_frame[0] = parity_bits["P1"]
orig_frame[1] = parity_bits["P2"]
orig_frame[3] = parity_bits["P3"]
orig_frame[7] = parity_bits["P4"]
orig_frame = "".join(orig_frame)
sleep(0.4)
print(f"\n{bright}{lcyan}Corrected Frame: ---{orig_frame[::-1]}---")