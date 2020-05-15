def run():
    a = int(input('Digite el primer número: '))
    b = int(input('Digite el segundo número: '))
    if a > b:
        print('El número mayor es: {} y la diferencia entre los números es: {}.'.format(a, a-b))
    elif b > a:
        print('El número mayor es: {} y la diferencia entre los números es: {}.'.format(b, b-a))
    else:
        print('Los números son iguales.')

if __name__ == '__main__':
    run()