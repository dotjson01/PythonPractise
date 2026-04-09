lsit = [29, "America", "Spain", True]

age, _, city, bo = lsit

print(age)
#print(_)
print(city)


# if you don't want that particular part 
list2 = [23, 'Data Engineering', True, 1.8, 0X212]

age, *_, hexcode = list2
print(list2)

print(*_)
print(age)
print(hexcode)