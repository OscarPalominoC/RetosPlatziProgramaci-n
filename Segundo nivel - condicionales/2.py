def run():
    a = int(input('Digite el valor límite: '))
    b = int(input('Digite el valor a evaluar: '))
    if a >= b:
        print('El número {} está dentro del límite.'.format(b))
    else:
        print('El número {} NO está dentro del límite.'.format(b))
    

if __name__ == '__main__':
    run()