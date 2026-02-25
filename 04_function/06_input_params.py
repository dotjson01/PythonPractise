chai = 'Ginger chai'

def fn_order(order):
    print(f" Preparing your order : {order}")

fn_order(chai)
print(f"Here is your order Please take it : {chai}")




# modifying list 

chai = [1, 12, 45]

def fn_list(chai_order):
    chai_order[1] = 45

fn_list(chai)
print(f" This is mutable code which is know as tuple :-> {chai}")


#positional and keyword

def positional(*ingredients, **extras):
    print(f" Ingredients -> {ingredients} ")
    print(f" Extras -> {extras} ")

positional("Panner", "Potato", spices="Haldi", powder= "Mirchi")
