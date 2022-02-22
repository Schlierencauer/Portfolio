while True:
    try:
        dlugosc =int(input('Podaj dlugosc miarki: '))
        kropki = ['|']
        cyfry = []
        for i in range(dlugosc):
            kropki.append('....|')
        for i in range(dlugosc+1):
            cyfry.append(str(i) + ' '*(5-len(str(i+1))))
        print(''.join(kropki) + '\n' + ''.join(cyfry))
    except ValueError:
        print('Podaj dlugosc w postaci liczby calkowitej')