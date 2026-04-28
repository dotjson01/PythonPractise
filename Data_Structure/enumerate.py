li = ['a','b','c']
print(enumerate(li)) # it will return object
print(list(enumerate(li))) # this will return list and object

print(list(enumerate(li, start=1))) # this will start from index 1 