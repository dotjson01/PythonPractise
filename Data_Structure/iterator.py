letters = ['a', 'b', 'c']
for l in letters:
    print(l) 


letters = [1, 2, 3]
for l in letters:
    print(l)



"""
letters = 123
for l in letters:
    print(l) 
""" 
'This will provide errors - > because it is not a sequence of items , iterable will be in sequence of items'


'This will not provide errors'
letters = 1,2,3
for l in letters:
    print(l)


for l in letters:
    print(l.upper())