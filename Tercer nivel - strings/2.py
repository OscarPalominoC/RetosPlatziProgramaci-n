def run():
    name = str(input('¿Cómo te llamas? '))
    lastname = str(input('¿Cuál es tu apellido? '))
    favFood = str(input('¿Cuál es tu comida favorita? '))
    print('Hola, mi nombre es {} {} y mi comida favorita es {}.'.format(name, lastname, favFood))

if __name__ == "__main__":
    run()