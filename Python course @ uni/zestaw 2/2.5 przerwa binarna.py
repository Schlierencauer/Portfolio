while True:
    def fun(N):
       list1 = [x for x in N[2:]]
       listaliczaca =[0]
       licznik = 0
       for i in list1:
           if i == '0':
               licznik = licznik + 1
               listaliczaca.append(licznik)
           else:
               licznik = 0
       print(max(listaliczaca))

    liczba = int(input('Podaj liczbe: '))
    if liczba < 1 or liczba > 2147483647:
        print('Poza zakresem')
    else:
        N = bin(liczba).rstrip('0')
        fun(N)