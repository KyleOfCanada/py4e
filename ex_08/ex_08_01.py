def chop(list) :
    list.pop(0)
    list.pop(len(list) - 1)
    print(list)
    return(None)

def middle(list) :
    list.pop(0)
    list.pop(len(list) - 1)
    return(list)

list1 = [1, 2, 3, 4, 5]
list2 = [0, 9, 8, 7, 6, 5]

print(chop(list1))
print(chop(list2))

print(middle(list1))
print(middle(list2))
