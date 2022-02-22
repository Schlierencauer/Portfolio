x = int(input('Podaj x: '))
y = int(input('Podaj y: '))
z = int(input('Podaj z: '))
n = int(input('Podaj n: '))
lista1 = [
         [i, j, k] for i in range(x+1)
                   for j in range(y+1)
                   for k in range(z+1)
                   if i + j + k != n
          ]
print(lista1)