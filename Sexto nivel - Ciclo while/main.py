import random
"""
Reto #1 - Suma hasta cincuenta

Crea una variable que se llame total, después pide a tu usuario que ingrese un número y lo sume al valor de total. Haz que esto se repita hasta que el valor de total sea mayor a 50 y muestra el resultado en pantalla.
"""
def reto_1():
    total = 0
    while(total <= 50):
        entrada = float(input('Ingresa un numero, me detendré hasta que la suma de estos sea mayor a 50: '))
        total += entrada
    print(f'El resultado final es {total}')

"""
Reto #2 - Más allá del cuarenta y dos

Crea un código que pida al usuario un número y se repita hasta que coloque un número mayor a 42. Cuando se cumpla esta condición muestra el resultado en pantalla indicando esto al usuario y finaliza el ciclo.
"""
def reto_2():
    n = 0
    while(n<=42):
        n = float(input('Ingresa un número... Dejaré de pedir numeros hasta que ingreses uno mayor a 42: ')
        )
    print(f'El numero que elegiste fue {n}')

"""
Reto #3 - Sumas consecutivas

Pide al usuario que ingrese dos números y los sume. Después pregunta si quiere añadir otro número: si la respuesta es afirmativa añádelo al total; en caso contrario finaliza el ciclo y muestra el resultado total en pantalla.
"""
def reto_3():
    numero_1 = float(input('Ingrese un numero: '))
    numero_2 = float(input('Ingrese otro numero: '))
    total = numero_1+numero_2
    response = input('Deseas ingresar otro numero? (S/N) ')
    while(response == 's' or response == 'S'):
        numero_n = float(input('Ingresa el numero: '))
        total += numero_n
        response = input('Deseas ingresar otro numero? (S/N) ')
    if response != 'n' or response != 'N':
        print('Esa opción no existe, te daré la suma de los numeros.')
    print(f'La suma de los numeros es {total}')

"""
Reto #4 - Lista de invitados

Estás organizando un banquete al que quieres invitar a tus amigos. Crea un programa que pida el nombre de uno de tus amigos, al hacerlo aumenta en uno una variable contadora, después pregunta si quieres invitar a alguien más: si la respuesta es afirmativa entonces pregunta por una persona más; en caso contrario cierra el ciclo y muestra en pantalla cuantos invitados son.
"""
def reto_4():
    lista_invitados = []
    response = input('Deseas agregar invitados al banquete? (S/N): ')
    while(response == 's' or response == 'S'):
        name = input('Escribe el nombre del invitado: ')
        lista_invitados.append(name)
        response = input('Deseas agregar más invitados al banquete? (S/N): ')
    if response != 'N' or response != 'n':
        print('Esa opción no existe. Te mostraré la lista de invitados si existe.')
    if len(lista_invitados) > 0:
        print(f'Hay en total {len(lista_invitados)} invitados al banquete.')
        print('Los nombres de los invitados son: ')
        for invitado in lista_invitados:
            print(f'Nombre: {invitado}')
    else:
        print('No hay invitados al banquete.')

"""
Reto #5 - Adivina el número secreto

Crea un programa donde tendrás la variable numero_secreto, la cual toma un valor aleatorio entre 1 y 100. Después pide a tu usuario que indique un número para intentar adivinarlo: en caso de acertar indícale cual era el número secreto y cuantos intentos le tomó; en caso contrario indícale si el número ingresado es mayor o menor al número secreto.
"""
def reto_5():
    print('Adivina el número secreto! está entre 1 y 100.')
    numero_secreto = random.randint(1, 100)
    counter = 0
    eleccion = 0
    while(eleccion != numero_secreto):
        eleccion = int(input('Elige un numero entre el 1 y el 100: '))
        counter+=1
        if eleccion == numero_secreto:
            print('Lo adivinaste!')
        elif eleccion < numero_secreto:
            print('Echale ganas, el numero que elegiste es muy pequeño.')
        else:
            print('Te pasaste! trata un poquito menos.')
    print(f"""
    El numero secreto era {numero_secreto}.
    Te tomó {counter} intentos para adivinar el número secreto.
    """)

"""
Reto #6 - “Un elefante se balanceaba…”

Escribe un programa que inicie mostrando en pantalla la letra de “Un elefante se balanceaba” iniciando con el número 1, después pregunta al usuario cuantos elefantes más se balancearán y debe responder un número más al mostrado. En caso de ingresar un número diferente pedirle que intente de nuevo y repetir el ciclo hasta tener 10 elefantes.
Tomar en cuenta cuando el texto muestra un solo elefante y varios elefantes.
Ejemplo de inicio:

1 elefante se balanceaba
Sobre la tela de una araña
Como veía que resistía
Fueron a llamar otro elefante
"""
def reto_6():
    elefantes = 1
    while elefantes <= 10:
        print(f"""
{elefantes} elefante se balanceaba
Sobre la tela de una araña
Como veía que resistía
Fueron a llamar otro elefante
        """)
        elefantes+=1
        if elefantes > 10:
            print('Ya no caben más elefantes!!')
            break
        cantidad = int(input('Cuántos elefantes se menearán ahora? '))
        if cantidad != elefantes:
            elefantes = 1

def main():
    eleccion = int(input("""
    Este programa te dará a elegir una serie de aplicaciones, elige la que desees.
    1 - Suma hasta cincuenta.
    2 - Más allá del cuarenta y dos
    3 - Sumas consecutivas
    4 - Lista de invitados
    5 - Adivina el número secreto
    6 - “Un elefante se balanceaba…”

    Cuál es tu elección? """))
    if eleccion < 1 or eleccion > 6:
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
    else:
        reto_6()


if __name__ == '__main__':
    main()