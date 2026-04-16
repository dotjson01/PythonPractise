list = [12, 10, 9, 8, 7] # insert() like someone cutting into a queue at a specific spot,  It adds an item at a specific position (index) that you choose.
list.insert(1, 11)
list.insert(2, 12)
print(list)
list.insert(2, 17)
print(list)


matrix =  [ 
    ['a', 'b', 'c'],
    ['d', 'e', 'f'], 
    ['g', 'h', 'i']
]

matrix.append(['j', 'k', 'l']) # a person joining queue at supermarket, adds a single item to the end of the list.
print(matrix)


matrix.insert(4, ['m', 'n', 'o'])
print(matrix)

#inserting number into particular index 
matrix[1].append('x')
print(matrix)

# insert z at starting of row 1 
matrix[1].insert(1,'z')
print(matrix)