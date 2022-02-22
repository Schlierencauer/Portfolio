lista1 = [[],[4],(1,2),[3,4,1],(5,6,7),[2]]
suma = []
print(len(lista1))
for i in range(len(lista1)):
    x = sum(lista1[i])
    suma.append(x)
print(suma)

