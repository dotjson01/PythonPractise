# nonlocal ->> Inside to inside function
# if you use this , enable to use inside the function 
# whatever the function made and used/active nonlocal , and then use variable of outside function the actual value modify 
# same as pass by reference 


# local scope
def outside_function():
    variable = "Elaichi"
    def inside_function():
        nonlocal variable 
        variable = "Lemon"
    inside_function()
    print(f"{variable}")


outside_function()



# global scope
chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irnai"
        print(f"{chai_type}")
    kitchen()

front_desk()




