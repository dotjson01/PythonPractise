f = 2
def multiple_factor(x):
    y=x*f
    return y

z= 6
print(z)






def clean_name(name):
    cleaned = name.strip().lower()
    return cleaned

print(clean_name) # it will gonna treat functions as object 
print(clean_name("Mar")) # it will gonna pass as argument which means following all parameters

cls=clean_name("Maria") #passing argument and storing the values into cls variable
print(cls)





def clean_name1(name):
    cleaned = name.strip().lower()
    # return cleaned
    'why returning [None] because we are not returning anything from the function as return disapperead from the function which carry whatever function do inside it '

print(clean_name1) # it will gonna treat functions as object 
print(clean_name1("Mar")) # it will gonna pass as argument which means following all parameters

cls=clean_name1("Maria") #passing argument and storing the values into cls variable
print(cls)



def clean_name2(name):
    if not name:
        return None
    cleaned = name.strip().lower()
    return cleaned

cls2 = clean_name2("")
print(cls2)
# currently i am not passing any kind of arguments here
# so that's why above return returning None 