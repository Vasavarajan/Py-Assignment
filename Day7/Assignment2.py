list1=[(1,2),(3,4),(5,6),(4,5)]
list2=[]
def add(x):
    return x[0]+x[1]
for i in range(len(list1)):
    x=list1[i]
    list2.append(add(x))
print(list2)