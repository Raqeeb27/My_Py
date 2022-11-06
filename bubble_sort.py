# Bubble sort.

def bubble_sort(list):
    for i in range(len(list) - 1):
        no_swap = True
        for j in range(len(list) - 1):
            if list[j + 1] < list[j]:
                temp = list[j]
                list[j]= list[j + 1]
                list[j + 1]= temp
                no_swap = False
        if no_swap:
            return


list = input('Enter the list of numbers: ').split()
list = [int(x) for x in list]
bubble_sort(list)
print('Sorted list: ', end='')
print(list)
