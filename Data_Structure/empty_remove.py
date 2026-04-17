list = [1, 2, 4, 5]
list.clear()  # we are using method () to clear up this list into empty list
print(list)

list2 = ['a', 'c', 'c', 'f', 'g']
list2.remove('c')
print(list2)


# pop or remove the item from last ones

list3 = ['q', 'w', 'e', 'r', 't', 'y']
list3.pop()
print(list3) # y is popped up from the list

# let's try with position popped
list3.pop(3)
print(list3)