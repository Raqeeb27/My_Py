-while True:
    terms = int(input("\nEnter no.of terms in fibonacci sequence: "))
    seq = []
    n1, n2 = 0, 1
    if terms <= 0:
        print("Please Enter positive number")
    elif terms == 1:
        print("Fibonacci sequence upto 1 term is:", [n1])
    else:
        print("The fibonacci sequence upto",terms , "terms is:")
        for i in range(terms):
            seq.append(n1)
            n = n1 + n2
            n1 = n2
            n2 = n
        print(seq)
    ch = input("\nDo you want to continue:(Y/N)\n")
    if ch == "y" or ch == "Y" or ch == "yes" or ch == "YES" or ch == "Yes":
        continue
    elif ch == "no" or ch == "NO" or ch == "No" or ch == "N" or ch == "n":
        break
    else:
        print("Inalid input\n")
        exit(0)
print("THANK YOU!!")
