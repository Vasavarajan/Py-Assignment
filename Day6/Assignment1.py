list1=[1,2,3,4,5,6,7]
list2=['a','s','d','e','f']
len1=min(len(list1),len(list2))
print( { list1[each] :list2[each] for each in range(len1)})
