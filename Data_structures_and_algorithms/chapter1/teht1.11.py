def combine_lists(list1,list2):
    clist = []
    for i in list1:
        clist.append(i)
    for j in list2:
        clist.append(j)
    clist.sort()
    return clist

list1 = [1,2,3,4,5,6]
list2 = [2,2,2,2,6]
print(combine_lists(list1,list2))