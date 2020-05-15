def run():
    a = int(input('Digite el límite superior: '))
    b = int(input('Digite el límite inferior: '))
    c = int(input('Digite el número a evaluar: '))
    if a >= c and b <= c:
        print('El número {} está dentro del rango permitido.'.format(c))
    elif c > a:
        print('El número {} está por encima del límite superior.'.format(c))
    else:
        print('El número {} está por debajo del límite inferior.'.format(c))

if __name__ == '__main__':
    run()