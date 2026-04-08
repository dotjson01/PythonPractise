lst = ['a', 'b', 'c', 'e']
print(lst)
print(lst[0])    #  a
print(lst[-1])   #  e
print(lst[2])    #  c

print(lst[:2])   # a, b 
print(lst[:])    # a, b, c, d
print(lst[:-1])  # a, b, c


matrix = [
    ['0', '1', '2'],
    ['3', '4', '5'],
    ['6','7', '8']
]

print(matrix[0:2]) # get the first two rows (lists) from a list
print(matrix[1:]) # get the last two rows (lists) from a list
print(matrix[2][0:2])