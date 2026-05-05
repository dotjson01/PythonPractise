# let;s try to work in dictionaries
my_list = {
    'a': 30,
    'b': 100,
    'c': 78,
    'f':45,
    'a':7800
    # as you can that it is overwritting the a value
}

print(my_list)
# dict is not INDEXED
# Values allow duplicates
# Key are unique
# Ordered

# print(my_list[1]) # it will be give error KEY ERRORS

# but if try to use with key , it will gonna show the values
print(my_list['b'])

# dict is keyed

my_list['c'] = 80
print(my_list) # set is mutuable

