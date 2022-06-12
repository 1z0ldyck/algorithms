arr = sorted([3,2,1,3, 3, 4, 4, 4 ,4, 1, 1, 2])

def velas_aniversario(arr):
    repetiu = 1
    anterior = repetiu
    for x in range(0, len(arr) - 1):
        if arr[x] == arr[x + 1]:
            repetiu += 1
        else:
            if repetiu > anterior:
                anterior = repetiu
                repetiu = 1
    if anterior > repetiu:
        return anterior
    return repetiu

print(velas_aniversario(arr))

        