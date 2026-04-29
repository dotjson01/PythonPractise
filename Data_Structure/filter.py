letters = ['a','', None, False, 'c', True, bool]
print(filter(None, letters))
print(list(filter(None, letters)))


items = ['sql', '123', 'python', '442']
# isalpha keeps only letters (alphabetic) items
c = list(filter(str.isalpha, items))
print(c)