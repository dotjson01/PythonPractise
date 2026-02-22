# you are manager a busy tea stall
# you recieve many orders and want to print each customer's name along with the type of chai they ordered
# write a function print_order(name, type)
# call it multiple times with different customers

def print_order(name, chai_type) :    # parameter used in function which take input from function call
     print(f"{chai_type} ordered by {name}")


print_order("Sahil", "Masala Chai") # function argument which basically pass the value to function name itself
print_order("Jiya", "Ginger Chai")
print_order("Tulsi", "Malai Chai") 