list = ['Maria', 29, 'Data Engineering', 'Spain']

name, age, role, country = list

print(list)
print(name)
print(age)


list2 = ['Maria', 29, 'Data Engineering', 'rich', 'millionarie', 'Spain']

name2, *details, country = list2


print(*details) # includes the between all items
print(country)



list3 = ['Maria', 29, 'Data Engineering', 'rich', 'millionarie', 'Spain']

*details, =list3

print(list3)
#print(name3)
print(*details)