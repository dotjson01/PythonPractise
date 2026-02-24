# scopes are basically called -> region 

# 1. Scope and name resolution
# 2 . local scope - inside the region
# 3. enclosing from outer fn if nested
# 4 . global is top of the script
# 5. built in 

def chai_counter() :
    chai_order = "Lemon"
    def print_order() :
        chai_order = "Ginger"
        print(f"Inside Function Chai : {chai_order}")
    print_order()

    print(f"Function : {chai_order}")

chai_order = "Global Chai"
chai_counter()
print(f"Global Chai : {chai_order}")