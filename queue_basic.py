from time import sleep

def create_queue():
    queue = []
    return queue

def enqueue():
    while True:
        element = input("Enter Element to Enqueue : ")
        if element == "":
            break
        queue.append(int(element))

def dequeue():
    sleep(0.5)
    while True:
        if not queue:
            print("Queue is Empty")
            break
        else:
            p = queue.pop(0)
            sleep(0.2)
            print(p," is removed from Queue")
            sleep(0.5)
            print(queue)
            sleep(0.5)
            proceed = input("Do you want to Dequeue further(Y/N): ")
            if proceed == 'y':
                continue
            else:
                break


def display():
    print(queue)

def quit():
    sleep(0.5)
    print("\nTHANK YOU")
    sleep(1)

def final_display():
    print("\nFinal Queue: ",queue)


queue = create_queue()
while True:
    choice = int(input("\nPlease Select the Operation\n\t1.ADD\n\t2.REMOVE\n\t3.SHOW\n\t4.QUIT\n"))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
            quit()
            break
    else:
        print("Invalid Operation")
    sleep(0.5)
    proceed = input("\nDo you want to proceed further operations(Y/N): ")
    if proceed == 'y' :
        continue
    else:
        sleep(0.5)
        final_display()
        break