import time
import random
import json
with open('tramwaje.json', "r", encoding='utf-8') as read_file:
    data = json.load(read_file)
    # print(data)
    lista_main = []
    for nr_tramwaju in data['tramwaje']:
        lista_przystanków = []
        # print(nr_tramwaju.get('name'))
        for przystanki in nr_tramwaju['tprzystanki'] :
            lista_przystanków.append(przystanki.get('name'))
            # print(przystanki.get('name'))
        lista_main.append(lista_przystanków)
        # break

    # print(lista_main)
    dic_przystanki = {}
    for lista_przystanków in lista_main:
        for j in range(0, len(lista_przystanków)):
            if lista_przystanków[j] not in dic_przystanki.keys():
                if j == 0:
                    dic_przystanki[lista_przystanków[0]] = {lista_przystanków[1]:1}
                else:
                    dic_przystanki[lista_przystanków[j]] = {lista_przystanków[j-1]:1}
        for j in range(len(lista_przystanków)-1,1,-1):
            dic_przystanki[lista_przystanków[j-1]].update({lista_przystanków[j]:1})

    # for keys in dic_przystanki.keys():
    #     dic_przystanki[keys] = set(dic_przystanki[keys])



    # print(len(dic_przystanki.keys()))
    # print(dic_przystanki.keys())
    # print(dic_przystanki.get('Teatr Bagatela'))
    # print(dic_przystanki)




    def dijkstra(dic_przystanki, start, cel):
        start_time = time.time()
        infinity = 9999
        dystans = {}
        poprzednik = {}
        nieOdwiedzone = dic_przystanki
        trasa = []

        for node in nieOdwiedzone:
            dystans[node] = infinity
        dystans[start] = 0

        while nieOdwiedzone:
            obecnyNode = None
            for node in nieOdwiedzone:
                if obecnyNode is None:
                    obecnyNode = node
                elif dystans[node] < dystans[obecnyNode]:
                    obecnyNode = node

            for następnyNode, waga in dic_przystanki[obecnyNode].items():
                if waga + dystans[obecnyNode] <= dystans[następnyNode]:
                    dystans[następnyNode] = waga + dystans[obecnyNode]
                    poprzednik[następnyNode] = obecnyNode
            nieOdwiedzone.pop(obecnyNode)
        # print(dystans)
        # print(poprzednik)

        currentNode = cel
        while currentNode != start:
            try:
                trasa.insert(0, currentNode)
                currentNode = poprzednik[currentNode]
            except KeyError:
                print('trasa niedostepna')
                break
        trasa.insert(0, start)
        if dystans[cel] != infinity:
            print(start, cel)
            print('Dystans to ' + str(dystans[cel]))
            print('Trasa to ' + str(trasa))
        print(time.time() - start_time, "seconds")

    dijkstra(dic_przystanki, random.choice(list(dic_przystanki.keys())), random.choice(list(dic_przystanki.keys())))

