while True:
    try:
        while True:
            i = int(input('Podaj poczatkowa liczbe gwiazdek (nieparzysta): '))
            if i%2 == 0:
                print('podałes liczbe parzysta')
                continue
            else:
                break
        gwiazdki = '*' * i
        for x in range(i):
            gwiazdki = (' ' * x + '*' * (int(i)-2*x))
            print(gwiazdki)
    except ValueError:
        print('Podaj liczbe calkowita')

