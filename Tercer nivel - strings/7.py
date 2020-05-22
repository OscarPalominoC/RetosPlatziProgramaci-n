def run():
    print('Traductor de Pig Latin')
    word = str(input('Introduzca la palabra a traducir: '))
    if word[0].lower() == 'a' or word[0].lower() == 'e' or word[0].lower() == 'i' or word[0].lower() == 'o' or word[0].lower() == 'u':
        translate = word + 'way'
    else:
        translate = word[1::] + word[0] + 'ay'
        translate = translate.capitalize()
    print(translate)

if __name__ == "__main__":
    run()