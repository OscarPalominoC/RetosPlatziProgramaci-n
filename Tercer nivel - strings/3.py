def run():
    print('Por favor, responde a las siguientes preguntas en minúsculas.')
    name = str(input('¿Cómo te llamas? '))
    lastname = str(input('¿Cuál es tu apellido? '))
    origin = str(input('¿En qué país naciste? '))
    print('Hola, tu nombre es {} {} y tu país de origen es {}.'.format(name.capitalize(), lastname.capitalize(), origin.capitalize()))

if __name__ == "__main__":
    run()