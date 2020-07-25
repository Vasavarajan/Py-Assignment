list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]
list3=list1+list2
print(list3)
list4=[]
for i in range(len(list3)):
    list4.append(min(list3))
    list3.remove(min(list3))
print(list4)