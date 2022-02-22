class Bug():
    licznik = 0
    def __init__(self):
        Bug.licznik = self.licznik + 1
        self.identyfikator = Bug.licznik
        print(self.identyfikator)

    def __str__(self):
        return ('Licznik = ' + str(Bug.licznik) + ' id= ' + str(id(self)))

    def __del__(self):
        self.__class__.licznik = self.licznik - 1
        print('Koniec, licznik = {}, identyfikator = {}'.format(Bug.licznik, self.identyfikator))


bugs = []
for i in range(10):
    bugs.append(Bug())
    print(bugs[-1])
