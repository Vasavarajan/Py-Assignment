list1=[(1,2,3),[1,2],['a','hit','less']]
list2=[]
for i in list1:
    for j in i:
        list2.append(j)

print(list2)
