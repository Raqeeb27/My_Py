from time import sleep

def create_stack():
    stack = []
    return stack

def check_empty():
    return len(stack) == 0

def push(stack,elements):
    stack.append(elements)

def pop(stack):
    if check_empty():
        print("Stack is Empty")
        print("\nFinal Stack : ", stack)
        exit()
    return stack.pop()

stack = create_stack()
while True:
    element = input("Enter Element to PUSH into Stack: ")
    if element == "":
        break
    push(stack,element)
print(stack)
while True:
    sleep(0.5)
    x = input("Do you want to pop an element(Y/N): ")
    if x == 'y':
        pop(stack)
        print("Stack after Popping an Element is : ",stack)
    else:
        print("\nFinal Stack : ",stack)
        break
