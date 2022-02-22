list1 =  [3, 4,[2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
licznik = 0
def deepDown(arg):

    for elem in arg:
        if isinstance(elem, list):
            deepDown(elem)
            global licznik
            if licznik < 1:
                licznik = licznik + 1
                elem.append(elem[(len(elem)-1)]+1)
                print(list1)


deepDown(list1)

