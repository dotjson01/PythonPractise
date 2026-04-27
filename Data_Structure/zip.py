alphabet = ['A', 'B', 'C', 'D']
letters = [1,2,3]
combo = zip(alphabet,letters)
print(combo)

# to convert this <zip object at 0x701c1e907c40> into list 
# we are going to use list(zip())

combo = list(zip(alphabet, letters))
print(combo)

# combinig a string character with other list
combo = list(zip(alphabet, letters, "Hello"))
print(combo)
'''it is only printing Hel because there are 3 character in both list so pairing of 3 '''