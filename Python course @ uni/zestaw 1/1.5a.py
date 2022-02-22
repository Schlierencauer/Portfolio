list1 = 'abdcef'
list2 = [1, 2, 'apples', 'cherrys', 'a', 'b', 'ab']
list3 = []
for i in list1:
    if i in list2:
        if i not in list3:
            list3.append(i)
print(list3)