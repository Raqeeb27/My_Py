# Selection_Sort

def selection_sort(list):
    for i in range(len(list) - 1):
        smallest = i
        for j in range(i + 1, len(list)):
            if list[j] < list[smallest]:
                smallest = j
        temp = list[i]
        list[i]= list[smallest]
        list[smallest]= temp


list = [int(x) for x in input('Enter the list of numbers: ').split()]
selection_sort(list)
print('Sorted list: ', end='')
print(list)