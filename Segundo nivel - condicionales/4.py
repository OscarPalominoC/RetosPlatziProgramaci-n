def run():
    animal = str(input('¿Cuál es tu animal favorito? '))
    if animal.lower() == 'tortuga' or animal.lower() == 'tortugas':
        print('También me gustan las tortugas.')
    else:
        print('Ese animal es genial, pero prefiero las tortugas.')

if __name__ == '__main__':
    run()