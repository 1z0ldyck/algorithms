array = input("Send array").split(' ')
target = int(input("Send target"))

for n in range(len(array)):
    element = array[n]
    for i in range(len(array)):
        if element + array[i] == target:
            print(element, i)
    


