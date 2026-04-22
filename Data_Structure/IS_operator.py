import copy

matrix = [
    ['a', 'b'], 
    ['c', 'd']
]

copy_matrix = matrix
print('Does it is pointing to same level', matrix is copy_matrix)