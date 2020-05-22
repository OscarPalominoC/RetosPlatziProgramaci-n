def run():
    name = str(input('¿Cómo te llamas? '))
    if len(name) <= 5:
        lastname = str(input('¿Cuál es tu apellido? '))
        print('Hola {} {}.'.format(name.capitalize(), lastname.capitalize()))
    else:
        print('Hola {}.'.format(name.capitalize()))

if __name__ == "__main__":
    run()