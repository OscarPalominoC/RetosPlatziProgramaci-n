def run():
    print('Vamos a calcular cuántas veces cabe un número menor a 100 en un número mayor a 1000 definido por el usuario')
    a = int(input('Digite un número mayor a 1.000: '))
    b = int(input('Digite un número menor a 100: '))
    return print('El número {} cabe {:.0f} veces dentro del número {}.'.format(b, a/b, a))

if __name__ == "__main__":
    run()