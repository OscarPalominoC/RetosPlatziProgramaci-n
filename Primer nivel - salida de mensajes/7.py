def run():
    name = str(input('Escribe tu nombre: '))
    age = int(input('¿Cuántos años tienes? '))
    return print('Hola {}, el año pasado tenías {} años, y el año entrante tendrás {} años.'.format(name, age -1, age +1))

if __name__ == '__main__':
    run()