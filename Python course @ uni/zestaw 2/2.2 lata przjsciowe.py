while True:
    try:
        def sprawdzacz_przetepnosci(rok):
            if rok % 4 == 0 and rok % 100 != 0:
                print(True)
            elif rok % 100 == 0 and rok % 400 == 0:
                print(True)
            else:
                print(False)
        rok = int(input('Podaj liczbe calkowita z zakresu 1900-10000: '))
        if rok < 1900 or rok > 10001:
            print('Poza zakresem')
            continue
        sprawdzacz_przetepnosci(rok)
    except ValueError:
        print('Wpisz liczbe calkowita')