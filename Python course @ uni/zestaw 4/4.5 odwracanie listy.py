lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
left = 0
right = 5
def odwracacz(lista,left, right):
    if left>1 :
        lista[left:right+1] = lista[right:left-1:-1]
    else:
        lista[left:right + 1] = lista[right::-1]
    print(lista)
odwracacz(lista,left, right)

