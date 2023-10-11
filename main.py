def print_hi(name):
    print(f'{name}')

def sum(n1, n2):
    print(n1+n2)

def print_orden():
    matriz = []
    for i in range(5):
        valor = int(input(f"Ingrese el valor {i + 1}: "))
        matriz.append(valor)
    matriz.sort()
    print("Elementos organizados:")
    for mat in matriz:
        print(mat)


def print_diagonal():
    matriz = [
        [2, 8, 6],
        [5, 7, 9],
        [4, 1, 6]
    ]
    suma = 0
    for i in range(3):
        for j in range(3):
            if(i==j):
                suma += matriz[i][j]
    print(suma)

def print_codigo_cesar(palabra):
    matriz = 'abcdefghijklmnopqrstuvwxyz'
    pala = ''
    for letra in palabra:
        if letra in matriz:
            indice = (matriz.index(letra) + 1) % 26
            pala += matriz[indice]
        else:
            pala += letra
    print(pala)

if __name__ == '__main__':
    print_hi('Hola Semana Tic')
    print(' \n')
    sum(5,2)
    print(' \n')
    # print_orden()
    # print(' \n')
    print_diagonal()
    print(' \n')
    print_codigo_cesar('casa')