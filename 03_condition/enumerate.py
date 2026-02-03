# enumerate function in python 
# each item must be numbered 
# use emumerate() to print menu items with numbers

menu_items = ["Dosa", "Idli", "Poori", "Upma"]
for  i in enumerate(menu_items) :
    print(f"{i} {menu_items}")

chai_menu = {"Masala", "Kadak", "Green"}
for idx , val in enumerate(chai_menu) :
    print(f"{idx}. {val}")