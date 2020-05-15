def run():
    print('Conversor de millas.')
    print('Convierte millas a kilometros.')
    distance = float(input('Digite la distancia a convertir: '))
    return print("En {} millas hay {:.2f} kilometros.".format(distance, (distance * 1.609344)))

if __name__ == "__main__":
    run()