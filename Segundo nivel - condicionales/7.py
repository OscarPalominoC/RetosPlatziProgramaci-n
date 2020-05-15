def run():
    print('¡ESCRIBE UN NÚMERO DEL 1 AL 6 Y OBTENDRÁS UN MENSAJE ALENTADOR!')
    selector = int(input('Digita tu opción: '))
    if selector == 1:
        print('Hoy aprenderemos sobre progamación.')
    elif selector == 2:
        print('¿Qué tal tomar un curso de marketing digital?')
    elif selector == 3:
        print('Hoy es un gran día para comenzar a aprender de diseño.')
    elif selector == 4:
        print('¿Y si aprendemos algo de negocios online?.')
    elif selector == 5:
        print('Veamos un par de clases sobre producción audiovisual.')
    elif selector == 6:
        print('Tal vez sea bueno desarrollar una habilidad blanda en Platzi.')
    else:
        print('¡ERROR! Enviaste una opción no válida.')

if __name__ == '__main__':
    run()