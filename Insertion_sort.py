# Insertion_Sort.

def insertion_sort(list):
    for i in range(1, len(list)):
        while (list[i-1] > list[i] and i>0):
            temp = list[i-1]
            list[i-1] = list[i]
            list[i] = temp
            i=i-1

list = [int(x) for x in input('Enter the list of numbers: ').split()]
insertion_sort(list)
print('Sorted list:',list)
