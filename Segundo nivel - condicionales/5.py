def run():
    rta = str(input('¿Está lloviendo? '))
    if rta.lower() == 'si' or rta.lower() == 'sí':
        rta = str(input('¿Está haciendo mucho viento? '))
        if rta.lower() == 'si' or rta.lower() == 'sí':
            print('Hace mucho viento para llevar una sombrilla.')
        else:
            print('Deberías usar una sombrilla.')
    else:
        print('Ten un lindo día.')

if __name__ == '__main__':
    run()