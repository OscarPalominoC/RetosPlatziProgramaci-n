def run():
    word1 = str(input('Escribe la palabra que estará totalmente en mayúsculas: '))
    word2 = str(input('Escribe la palabra que estará totalmente en minúsculas: '))
    print('La(s) palabra(s) 1 es {}, la(s) palabra(s) 2 es {}.'.format(word1.upper(), word2.lower()))

if __name__ == "__main__":
    run()