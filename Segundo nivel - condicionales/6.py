def run():
    a = int(input('Digite su edad: '))
    if a >= 30:
        print('Nunca es tarde para aprender ¿Qué curso tomaremos?')
    elif a >= 18 and a < 30:
        print(' Es un momento excelente para impulsar tu carrera.')
    elif a>= 0 and a < 18:
        print('¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte.')
    else:
        print('¿Seguro que siquiera deberías existir?')

if __name__ == '__main__':
    run()