"""
Reto #1 - Curso favorito

Pide a tu usuario que indique cual es su curso favorito de Platzi e imprímelo en pantalla 8 veces.
¿Por qué 8 veces? Porque este año Platzi cumplió 8 años 😉
"""
def reto_1():
    curso = input('Cuál es tu curso favorito? ')
    for i in range(8):
        print(curso)
    return 0


"""
Reto #2 - Curso favorito ‘n’ veces

Toma el reto anterior, pero ahora pregunta al usuario cuantas veces quiere mostrar el mensaje.
¿Qué pasa si coloca cero como respuesta? 🤔
"""
def curso_favorito(curso, repeticion):
    if repeticion == 0:
        print('No habrá repeticiones :(')
    else:
        for i in range(repeticion):
            print(curso)
    return 0

def reto_2():
    curso = input('Cuál es tu curso favorito? ')
    repeticion = int(input('Cuántas veces se repetira el mensaje? '))
    return curso_favorito(curso, repeticion)

"""
### Reto #3 - Curso en una columna
Nuevamente, pide a tu usuario que indique su curso favorito de Platzi pero ahora muestra un caracter por línea de forma que puede parecer el inicio de un acróstico.
"""
def reto_3():
    curso = input('Cuál es tu curso favorito? ')
    for i in curso:
        print(i)
    return 0


"""
Reto #4 - Animal en columna ‘n’ veces.

Toma como base el reto anterior, pide a tu usuario que indique su animal favorito y después muéstralo con un caracter por línea. Esto debe repetirse un número de veces que ya hayas preguntado a tu usuario.
"""
def reto_4():
    animal = input('Cuál es tu animal favorito? ')
    repeticiones = int(input('Cuántas veces se repetira? '))
    if repeticiones == 0:
        print('No habrá repeticiones :(')
    else:
        for i in range(repeticiones):
            print(f'Ciclo # {i+1}')
            for a in animal:
                print(a)
    return 0

"""
Reto #5 - Tabla de multiplicar

Pide a tu usuario un número, luego de ello muestra la tabla de multiplicar de ese número del 1 al 10.
"""
def reto_5():
    tabla = int(input('Cual tabla de multiplicar quieres ver? '))
    for i in range(10):
        print(f'{tabla} * {i+1} = {tabla*(i+1)}')
    return 0

"""
Reto # 6 - Cuenta regresiva

Pide a tu usuario un número, después imprime una cuenta regresiva uno a uno, desde ese número hasta 0. Esto aplica también para números negativos.
"""
def reto_6():
    numero = int(input('Elige un numero para hacer la cuenta regresiva hasta el cero: '))
    if numero > 0:
        for i in range(numero+1):
            print(numero-(i))
    else:
        for i in range(abs(numero-1)):
            print(numero+(i))
    return 0

"""
Reto #7 - Curso favorito, sin exagerar

Toma como base el Reto #2, pero agrega como condiciones las siguientes:

    Si el número ‘n’ es mayor a 15, solo imprimirás el nombre del curso 3 veces e indicarás que ‘n’ es un número muy grande.
"""
def reto_7():
    curso = input('Cuál es tu curso favorito? ')
    repeticion = int(input('Cuántas veces se repetira el mensaje? '))
    if repeticion > 15:
        print(f'{repeticion} es un numero muy grande. Lo repetiremos 3 veces.')
        return curso_favorito(curso, 3)
    else:
        return curso_favorito(curso, repeticion)

"""
### Reto #8 - Suma autorizada
Crearás un programa que pedirá a tu usuario 4 números, uno por uno. Al indicarlo preguntarás al usuario si desea sumarlo al total, si la respuesta es afirmativa se sumará. Al final debes mostrar el valor de la suma de aquellos números que fueron aceptados para la suma.
"""
def reto_8():
    suma = 0
    for i in range(4):
        numero = float(input('Ingresa un numero: '))
        decision = input('Quieres que este numero se añada a una suma? (S/N): ')
        if decision == 'S' or decision == 's' or decision == 'si' or decision == 'SI':
            suma += numero
        elif decision != 'N' or decision != 'n' or decision != 'no' or decision != 'NO':
            print('Esa no es una eleccion correcta. No lo sumaremos.')
    return print(f'El total de los numeros sumados es {suma}')

"""
Reto #9 - Recta numérica

Escribe un programa donde preguntes a tu usuario si desea una recta numérica positiva o negativa, después pide un número que servirá como límite e imprime todos los números de uno en uno partiendo desde el cero.
"""
def reto_9():
    eleccion = input('Quieres una recta numerica positiva (P) o negativa (N)? (P/N)')
    limite = int(input('Cual sera el limite? '))
    if eleccion == 'P' or eleccion == 'p':
        for i in range(limite+1):
            print(i)
    if eleccion == 'N' or eleccion == 'n':
        for i in range(abs(limite-1)):
            print(-i)
    else:
        print('Esa elección no es posible, no haremos la recta numérica.')
    return 0

def main():
    eleccion = int(input("""
    Este programa te dará a elegir una serie de aplicaciones internas, selecciona la que más te guste.

    1. Curso favorito.
    2. Curso favorito ‘n’ veces
    3. Curso en una columna
    4. Animal en columna ‘n’ veces.
    5. Tabla de multiplicar
    6. Cuenta regresiva
    7. Curso favorito, sin exagerar
    8. Suma autorizada
    9. Recta numérica
    
    ¿Cuál es tu elección?
    """))
    if eleccion < 1 or eleccion > 9:
        print('Esa elección no existe.')
        exit()
    elif eleccion == 1:
        reto_1()
    elif eleccion == 2:
        reto_2()
    elif eleccion == 3:
        reto_3()
    elif eleccion == 4:
        reto_4()
    elif eleccion == 5:
        reto_5()
    elif eleccion == 6:
        reto_6()
    elif eleccion == 7:
        reto_7()
    elif eleccion == 8:
        reto_8()
    else:
        reto_9()


if __name__ == '__main__':
    main()
    