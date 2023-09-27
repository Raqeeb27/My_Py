while True:
    sequence = []
    n1, n2 = 0, 1
    try:
        terms = int(input("\nEnter desired number of terms of Fibonacci sequence: "))
    except ValueError:
        print("\nInvalid Input\nPlease enter Positive Integer\n")
        continue

    if terms <= 0:
        print("\nPlease enter Positive Integer")
    elif terms == 1:
        print(f"\nFibonacci sequence upto 1 term is:\n[{n1}]")
    else:
        print(f"\nThe Fibonacci sequence upto {terms} terms is:")
        for i in range(terms):
            sequence.append(n1)
            n = n1 + n2
            n1 = n2
            n2 = n
        print(sequence)

    choice = input("\nDo you want to continue:(Y/N): ").upper()

    if choice in ["YES","Y"] :
        print()
        continue
    elif choice in ["NO","N"] :
        break
    else:
        print("Invalid Input\n")
        exit()

print("THANK YOU!!")
