original_list = ['a', 'b', 'c']
cpy_list = original_list.copy()
cpy_list.append('f')
print(original_list) # this is the different memory pointing to
print(cpy_list) # this is another memory pointing to

# this is called shallow copy , which means does'nt effect to original ones
