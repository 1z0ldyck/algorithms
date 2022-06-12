lista = [1,1,1, 0, -1, -1, 1, 3]

def percorre_array(array):

    negativos = ''
    positivos = ''
    pos_negativo = ''

    for i in enumerate(array, 1):
        print(i)
        if i[1] == 0:
            negativos = i[0] - 1
            positivos = len(array) - i[0]
            print(positivos, negativos)
            return positivos, negativos
        elif i[1] < 0:
            pos_negativo = i[0]

    if positivos == '':
        positivos = pos_negativo - 1
        return positivos, negativos


def proporcao(array):
    novo_array = sorted(array)
    tamanho_array = len(novo_array)
    par_ou_impar = 'par' if len(novo_array) % 2 == 0 or len(novo_array) - 1 % 2 == 0 else 'impar'

    if par_ou_impar == 'par':
        metade = round(tamanho_array / 2)
    else:
        metade = round(tamanho_array / 2) - 1

    if novo_array[metade] == 0:
        negativos = metade
        positivos = len(array) - metade - 1
        return positivos, negativos
    else:
        return percorre_array(novo_array)



print(proporcao(lista))
