def run():
    inicial = int(input('¿Cuántas porciones de pizza ordenarás? '))
    print('El repartidor de pizza llegó. Te trajó {} porciones de pizza.'.format(inicial))
    consumidas = int(input('¿Cuántas porciones de pizza han comido? '))
    return print("Aún quedan {} porciones de pizza.".format(inicial - consumidas))

if __name__ == '__main__':
    run()