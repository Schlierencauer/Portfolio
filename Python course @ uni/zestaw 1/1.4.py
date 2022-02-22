while True:
    try:
        szerokosc = int(input('Podaj jaka szerokosc ma miec prostokat: '))
        dlugosc = int(input('Podaj jaka dlugosc ma miec prostokat: '))
        poziomo = ['+']
        pionowo = ['|']
        for i in range(szerokosc):
            poziomo.append('---+')
            pionowo.append('   |')

        print((''.join(poziomo) + '\n' + ''.join(pionowo) + '\n' )* dlugosc + ''.join(poziomo))
        break
    except ValueError:
        print('Podane parametry musza byc liczba calkowita!')