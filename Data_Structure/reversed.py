lis = ['a', 'b', 'c']
num = [1, 2, 3]
print(reversed(lis))

print(list(reversed(lis)))

# you can use the iterator 
for l in reversed(lis):
    print(l)


# you can use a zip also
print(zip(reversed(lis)))
print(list(zip(lis,num))) # [('a', 1), ('b', 2), ('c', 3)]
print(list(zip((lis,num)))) # [(['a', 'b', 'c'],), ([1, 2, 3],)]

for l, n in zip(lis, num):
    print(l,n)