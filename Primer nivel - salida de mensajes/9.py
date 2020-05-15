def run():
    print('Calculando el tiempo en un número de días determinado por ti.')
    days = int(input('Digite la cantidad de días a calcular: '))
    print('La cantidad de horas en {} días son: {}'.format(days, days*24))
    print('La cantidad de minutos en {} días son: {}'.format(days, days*24*60))
    print('La cantidad de segundos en {} días son: {}'.format(days, days*24*60**2))

if __name__ == "__main__":
    run()