list1 = 'abdcef'
list2 = [1, 2, 'apples', 'cherrys', 'a', 'b', 'ab']
list3=[]
for i in list1:
    list3.append(i)
for i in list2:
    list3.append(i)

for i in list3:
    if list3.count(i) >1:
        list3.remove(i)
print(list3)