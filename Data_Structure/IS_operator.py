import copy

matrix = [
    ['a', 'b'], 
    ['c', 'd']
]

# assignement
copy1 = matrix
print('Does it is pointing to same level', matrix is copy1)

# shallow copy
copy2 = matrix.copy()
print('Same object', matrix is copy2)
print('Same list', matrix)

# deep copy
copy2 = matrix.copy()
copy3 = matrix.copy()
copy3