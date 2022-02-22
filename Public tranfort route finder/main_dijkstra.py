import time
import random
import json


with open('trams.json', "r", encoding='utf-8') as read_file:
    data = json.load(read_file)
    # print(data)
    lista_main = []
    for nr_of_tram in data['tramwaje']:
        list_of_stops = []
        # print(nr_of_tram.get('name'))
        for stops in nr_of_tram['tprzystanki'] :
            list_of_stops.append(stops.get('name'))
            # print(stops.get('name'))
        lista_main.append(list_of_stops)
        # break

    # print(lista_main)
    dic_stops = {}
    for list_of_stops in lista_main:
        for j in range(0, len(list_of_stops)):
            if list_of_stops[j] not in dic_stops.keys():
                if j == 0:
                    dic_stops[list_of_stops[0]] = {list_of_stops[1]:1}
                else:
                    dic_stops[list_of_stops[j]] = {list_of_stops[j-1]:1}
        for j in range(len(list_of_stops)-1,1,-1):
            dic_stops[list_of_stops[j-1]].update({list_of_stops[j]:1})

    # for keys in dic_stops.keys():
    #     dic_stops[keys] = set(dic_stops[keys])



    # print(len(dic_stops.keys()))
    # print(dic_stops.keys())
    # print(dic_stops.get('Teatr Bagatela'))
    # print(dic_stops)




    def dijkstra(dic_stops, start, cel):
        start_time = time.time()
        infinity = 9999
        distance = {}
        previous_stop = {}
        not_visited = dic_stops
        route = []

        for node in not_visited:
            distance[node] = infinity
        distance[start] = 0

        while not_visited:
            current_node = None
            for node in not_visited:
                if current_node is None:
                    current_node = node
                elif distance[node] < distance[current_node]:
                    current_node = node

            for nextNode, weight in dic_stops[current_node].items():
                if weight + distance[current_node] <= distance[nextNode]:
                    distance[nextNode] = weight + distance[current_node]
                    previous_stop[nextNode] = current_node
            not_visited.pop(current_node)
        # print(distance)
        # print(previous_stop)

        currentNode = cel
        while currentNode != start:
            try:
                route.insert(0, currentNode)
                currentNode = previous_stop[currentNode]
            except KeyError:
                print('route not available')
                break
        route.insert(0, start)
        if distance[cel] != infinity:
            print(f'{start} --> {cel}')
            print(f'Distace is {str(distance[cel])} stops')
            print(f'Route is {str(route)}')
        print(f'Search took {time.time() - start_time} seconds')

    dijkstra(dic_stops, random.choice(list(dic_stops.keys())), random.choice(list(dic_stops.keys())))

