numbers = ['1', '2', '3', '5']
letters = [1,2,3]
combo = zip(numbers,letters)
print(combo)

# to convert this <zip object at 0x701c1e907c40> into list 
# we are going to use list(zip())

combo = list(zip(numbers, letters))
print(combo)
