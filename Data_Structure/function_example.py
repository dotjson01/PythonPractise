# now dealing with functions

def make_coffee():
    print("Start Machine")
    print("Make Coffee")
    print("Add Milk")
    print("Enjoy it")


print("Wake Up")
make_coffee()
print("Working for a While")
make_coffee()
make_coffee()


# Built-in Function (Just Calling )
print(len("Python"))

# Function From Libraries
import math
number = 2.4
'''
 print(ciel(number)) # python don't understand the ciel , so we need to import library to activate this word
'''
print(math.ceil(number))


# User-defined function
def greet():
    print('Hello')

greet()