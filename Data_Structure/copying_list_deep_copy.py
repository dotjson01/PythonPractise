# creat a copy of the list in a new variable
original_list = ['a', 'b', 'c', 'd']
cpy_list= original_list # reference list 

cpy_list.append('e')
print(cpy_list)
print(original_list)

# both list referencing the same memory list

# in the above it is doing shallow copy but now we are doing deep copy

import copy
matrix =[
    ['a', 'b'],
    ['c', 'd']
]

matrix_copy = copy.deepcopy(matrix)
matrix.pop()

# now if you try to do something in matrix_copy , won't effect on original ones
matrix_copy[0].append('z')
print(matrix)
print(matrix_copy)