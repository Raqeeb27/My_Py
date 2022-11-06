from time import *

print("ADDITION OF MATRICES")

sleep(0.5)

a = [int(x) for x in input("Enter elements of Matrix A : ").split()]
b = [int(x) for x in input("Enter elements of Matrix B : ").split()]

while len(a) != len(b) and len(a) < len(b):
    a.append(0)
while len(a) != len(b) and len(a) > len(b):
    b.append(0)

sleep(0.5)

print("ln(a)=", len(a), "len(b)=", len(b))

c = []

for i in range(len(a)):
    c.append(a[i] + b[i])

sleep(0.5)

print("The Sum of Matrix A and Matrix B is :", c)
