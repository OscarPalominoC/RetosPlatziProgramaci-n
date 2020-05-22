def run():
    fragment = str(input('Escribe o pega acá un fragmento de una oración, poema o lo que quieras: '))
    begin = int(input('¿Desde qué caracter deberíamos empezar? '))
    end = int(input('¿Hasta qué caracter deberíamos terminar? '))
    print(fragment[begin-1:end])

if __name__ == "__main__":
    run()