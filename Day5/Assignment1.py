list1=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
list2=[]
list3=[]

for i in list1:
    if i==0:
        list2.append(i)
    else:
        list3.append(i)
print(sorted(list3)+list2)