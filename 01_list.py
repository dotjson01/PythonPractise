# list [ expression for item in iterable if condition]
# list comprehension is concise way to create list in python using single line of code

menu = ["Dosa making", "Idli Dosa", "Poori and chai", "Upma"]

tea_menu = [item for item in menu if "chai" in item]
print(tea_menu)


menu1 = ["Dosa making", "Idli Dosa", "Poori and chai", "Upma"]

tea_menu1 = [item1 for item1 in menu1 if "Dosa" in item1]
print(tea_menu1)


tea_menu2 = [item2 for item2 in menu1 if len(item2) > 13]
print(tea_menu2)