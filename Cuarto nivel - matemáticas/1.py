import math
"""
Reto #1 - Multiplicar decimales

Pide a tu usuario que ingrese 2 números con decimales (cuantos más mejor) y muestra el resultado de multiplicarlos ¿fácil, no?
"""
def reto_1():
    print('Ingresa 2 números decimales y te mostraré el producto de ellos.')
    numero_1 = float(input('Ingrese el primer decimal (utiliza el punto): '))
    numero_2 = float(input('Ingrese el segundo decimal (utiliza el punto): '))
    return print(f'El resultado de multiplicar {numero_1} por {numero_2} es {numero_1*numero_2}')

"""
### Reto #2 - Reducir los decimales
Toma como base el reto anterior, pero ajústalo para que el resultado muestre solamente 1, 2, 3 o 4 decimales.
"""
def reto_2():
    print('Ingresa 2 números decimales y te mostraré el producto de ellos con 2 decimales.')
    numero_1 = float(input('Ingrese el primer decimal (utiliza el punto): '))
    numero_2 = float(input('Ingrese el segundo decimal (utiliza el punto): '))
    return print(f'El resultado de multiplicar {numero_1} por {numero_2} es {round(numero_1*numero_2,2)}')


"""
Reto #3 - Raíces cuadradas redondeadas

Pide a tu usuario que ingrese un número, cuyo valor debe ser mayor a 20, luego calcula su raíz cuadrada y reduce a 2 o 3 decimales el resultado final.
"""
def reto_3():
    print('Ingresa un número mayor a 20 y te calcularé su raíz cuadrada con 3 decimales :)')
    numero = float(input('Escribe tu número: '))
    if numero < 20:
        print('El numero que elegiste es mejor a 20. Lo siento, no podemos continuar.')
        exit()
    return print(f'La raíz cuadrada de {numero} es {round(math.sqrt(numero), 3)}')

"""
Reto #4 - Calcular área de un círculo

Solicita a tu usuario que ingrese un número el cual será el radio de un círculo y con este dato calcula el área de un círculo.
Si tu lenguaje cuenta con librerías específicas para este propósito haz uso de las mismas.
"""
def reto_4():
    print('Ingresa un número, lo tomaré como el radio de un círculo y te calcularé el área con 3 decimales :)')
    numero = float(input('Ingresa el radio del círculo: '))
    return print(f'El área del circulo con radio {numero} es {round(math.pi*(numero**2), 3)}')

"""
Reto #5 - Calcular volumen de un cilindro

Pide a tu usuario que indique el radio y la profundidad de un cilindro. Después aplica la fórmula correspondiente para calcular el volumen del cilindro y reduce el resultado a un solo decimal.
"""
def reto_5():
    print('Dame el radio de la base de un cilindro y su profundidad y te calcularé el volumen de este con 1 decimal :)')
    radio = float(input('Escribe el valor del radio de la base del cilindro: '))
    profundidad = float(input('Escribe la profundidad del cilindro: '))
    return print(f'El volumen del cilindro con radio {radio} y profundidad {profundidad} es {round(math.pi * radio**2 * profundidad, 1)}')

"""
Reto #6 - Mostrar enteros y residuos

Pide al usuario que ingrese 2 números, divídelos, muestra un resultado como enteros y además el residuo por separado de una forma que seal fácil de entender al usuario.
Por ejemplo: “9 dividido entre 2 es 4 y sobra 1”.
"""
def reto_6():
    print('Ingresa 2 números, los dividiré y te mostraré el resultado y el residuo :)')
    dividendo = int(input('Ingresa el dividendo: '))
    divisor = int(input('Ingresa el divisor: '))
    return print(f'{dividendo} dividido entre {divisor} es {dividendo//divisor} y sobra {dividendo%divisor}')

"""
Reto #7 - Calcular perímetros y áreas

Muestra un menú con distintas figuras geométricas, por lo menos 3 diferentes (triángulo, cuadrado, pentágono, etc.)
Tu usuario debe poder elegir alguna de estas figuras, indicar la distancia de sus lados y mostrar como resultado tanto el perímetro como el área de dicha figura.
"""
def reto_7():
    print("""
    De las siguientes figuras geométricas, elige 1 y te calcularé su área y perímetro.
    1. Triángulo rectángulo.
    2. Cuadrado.
    3. Pentágono regular.
    4. Rectángulo.
    """)
    eleccion = int(input('Cuál es la figura de tu elección?: '))
    if eleccion < 1 or eleccion > 4:
        print('Esa elección no existe.')
        exit()
    elif eleccion == 1:
        lado_1 = float(input('Cuál es el valor del cateto opuesto?: '))
        lado_2 = float(input('Cuál es el valor del cateto adyacente?: '))
        figura = 'triángulo rectángulo'
        hipotenusa = math.sqrt(lado_1**2 + lado_2**2)
        perimetro = lado_1+lado_2+hipotenusa
        area = (lado_1*lado_2)/2
    elif eleccion == 2:
        figura = 'cuadrado'
        lado = float(input('Cuál es el valor del lado del cuadrado? '))
        perimetro = lado*4
        area = lado**2
    elif eleccion == 3:
        figura = 'pentágono regular'
        lado = float(input('Introduzca el valor del lado del pentágono regular: '))
        apotema = lado/(2*math.tan(math.radians(36)))
        perimetro = 5*lado
        area = (perimetro*apotema)/2
    else:
        figura = 'rectángulo'
        base = float(input('Introduzca el valor de la base: '))
        altura = float(input('Introduzca el valor de la altura: '))
        perimetro = 2*base + 2*altura
        area = (base*altura)/2

    return print(f"""
    La figura {figura} tiene estos resultados:
    Perímetro = {round(perimetro, 2)}
    Área = {round(area, 2)}

    """)

def main():
    eleccion = int(input("""
    Este programa te dará a elegir entre una serie de aplicaciones matemáticas, selecciona la que desees.
    1. Multiplicar decimales: Ingrese 2 números con decimales (cuantos más mejor) y muestra el resultado de multiplicarlos ¿fácil, no?
    2. Reducir los decimales. Tomamos como base el reto anterior, pero ajustamos para que el resultado muestre solamente 2 decimales.
    3. Raíces cuadradas redondeadas. Ingrese un número cuyo valor debe ser mayor a 20, luego el programa calcula su raíz cuadrada y reduce a 3 decimales el resultado final.
    4. Calcular área de un círculo. Ingrese un número el cual será el radio de un círculo y con este dato calcula el área de un círculo.
    5. Calcular volumen de un cilindro. Indica el radio y la profundidad de un cilindro. Después el programa aplicará la fórmula correspondiente para calcular el volumen del cilindro y reduce el resultado a un solo decimal.
    6. Mostrar enteros y residuos. Ingrese 2 números, el programa los dividirá y mostrará un resultado como enteros y además el residuo por separado de una forma que seal fácil de entender al usuario.
    7. Calcular perímetros y áreas. Seleccionarás una lista de figuras geométricas, de la figura se te pedirá que ingreses valores y te devolverá el perímetro y el área de la figura.
    Cuál es tu elección?: 
    """))
    if eleccion < 1 or eleccion > 7:
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
    else:
        reto_7()
    
if __name__ == '__main__':
    main()