array = [[3], [11,2,4], [4,5,6], [10,8,-12]]

def tamanho(elem):
    return len(elem)

def differenceDiagonal(array):
    array.sort(key=tamanho, reverse=True)
    calc_diagonal_1 = sum([array[i][i] for i in range(0, len(array)) if len(array[i]) > 2])
    for i in range(0, len(array)):
        array[i] = list(reversed(array[i]))
    calc_diagonal_2 = sum([array[i][i] for i in range(0, len(array)) if len(array[i]) > 2])
    diff = calc_diagonal_1 - calc_diagonal_2
    return diff







