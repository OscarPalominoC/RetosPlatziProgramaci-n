def run():
    a = float(input('Digite el primer número: '))
    b = float(input('Digite el segundo número: '))
    c = float(input('Digite el multiplicador número: '))
    return print("{0:.2f}".format((a+b)*c))


if __name__ == '__main__':
    run()