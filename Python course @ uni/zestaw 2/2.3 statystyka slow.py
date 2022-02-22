napis = 'slowo1   slowo2 slowo3 .,?!!!  "slowo4"'
listaZnakow = ['.', ',', ':', ';', '!', '?', '...', '-', '(', ')', '[', ']', '{', '}', '<', '>' , "'" , '"']
slownik_liter = {}
for znak in napis:
    if znak in listaZnakow:
        napis = napis.replace(znak, '')

slowa = napis.split()

print('Liczba slow to: ' + str(len(slowa)))
ilosc_liter = 0
for i in range(len(slowa)):
    ilosc_liter = ilosc_liter + len(slowa[i])
print('Liczba liter to: ' + str(ilosc_liter))


for znak in napis:
    slownik_liter.setdefault(znak, 0)
    slownik_liter[znak] = slownik_liter[znak] + 1
print(slownik_liter)