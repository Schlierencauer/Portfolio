def roman2int(liczba):
    roman = {
        'I' : 1, 'V' : 5, 'X' : 10,
        'L' : 50, 'C' : 100, 'D' : 500,
        'M' : 1000
        }

    # roman = dict([('I', 1), ('V', 5), ('X', 10),
    #               ('L', 50), ('C', 100), ('D', 500),
    #               ('M', 1000)])

    # rzymskie = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    # arabskie = [1, 5, 10, 50, 100, 500, 1000]
    # roman = dict(zip(rzymskie, arabskie))

    licznik = 0

    for i in range(len(liczba)):
        if i > 0 and roman[liczba[i]] > roman[liczba[i-1]]:
            licznik += roman[liczba[i]] - 2 * roman[liczba[i-1]]
        else:
            licznik += roman[liczba[i]]
    print(licznik)


liczba = input('Podaj liczbe rzymska: ').upper()
roman2int(liczba)