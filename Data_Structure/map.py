letters = ['a', 'b', 'c']
c=list(map(str.upper, letters))
print(c)


numbers = ['1', '2', '3']
print(list(map(int, numbers)))

numbers = [1, 2, 3]
print(list(map(str, numbers)))


names = [' Marai', 'Lal ', ' Kumar ']
print(list(map(str.strip, names))) 
# this is used to remove unwanted space and clean the data