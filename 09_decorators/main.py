#  decorators means decoration on the top layer   for example -> making love on coffee upper layer
# it is wrapper around function 
#  


def my_function (func):
    def wrapper():
        print("Before the function ")
        func()
        print("After the function")
    return wrapper


@my_function
def greet():
    print("Hello Greet From Everyone")

greet()