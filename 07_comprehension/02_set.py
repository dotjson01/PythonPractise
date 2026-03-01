# set { expression for item in iterable if condition}
# set comprehension is concise way to create set in python using single line of code

menu = {"Dosa making", "Idli Dosa", "Poori and chai", "Upma", "Dosa making", "Idli Dosa"}

tea_menu = {item for item in menu}
print(tea_menu)


# finding the unique spices in all recipes
recipes = {
    "Masala Chai" : ["ginger", "cardmon", "cinnamon"],
    "Kadak Chai" : ["ginger", "cardmon", "cinnamon", "cloves"],
    "Green Chai" : ["ginger", "cardmon", "cinnamon", "cloves", "green cardmon"]
}

unique_spices = {spice for recipe in recipes.values() for spice in recipe}
#  this is called nested comprehension
#  as first it will gonna run for recipe in recipes.values() and then for spice in recipe 
# and then it will gonna store in unique_spices
print(unique_spices)