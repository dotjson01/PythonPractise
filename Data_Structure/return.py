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