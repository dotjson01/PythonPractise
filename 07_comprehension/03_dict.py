# dict {key : value for item in iterable if condition}
# dict comprehension is concise way to create dict in python using single line of code

menu = {
    "Dosa" : 100,
    "Idli" : 50,
    "Poori" : 200,
    "Upma" : 150
}

#  i want to convert this into dollar 
dollar_menu = {item : price * 0.012 for item, price in menu.items()}
# read like this price in menu.items() and traversing through each item (for loop) and multiplying with 0.012
print(f"${dollar_menu}")