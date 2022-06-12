def calcula(array):
    novo_array = sorted(array)
    soma_minima = sum([novo_array[x] for x in range(0, len(novo_array) - 1)])
    soma_maxima = sum([novo_array[x] for x in range(1, len(novo_array))])
    return soma_minima, soma_maxima

print(calcula([1,3,5,7, 9]))