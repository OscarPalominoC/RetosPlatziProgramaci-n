def run():
    print('¡Saliste con tus amigos, y es hora de pagar!')
    quantity = int(input('¿Con cuántas personas saliste? '))
    payment = float(input('¿Cuánto es el total a pagar? '))
    tips = float(input('¿Cuál es el porcentaje de propina por la atención? '))
    taxes = float(input('¿Cuál es el porcentaje de impuestos a pagar? '))
    tips = payment * tips / 100
    taxes = payment * taxes / 100
    total = payment + tips + taxes
    print('La propina a pagar es: {}'.format(tips))
    print('Los impuestos a pagar son: {}'.format(taxes))
    print('El total a pagar es: {}'.format(total))
    print('Cada uno debe pagar: {}'.format(total/quantity))

if __name__ == "__main__":
    run()
