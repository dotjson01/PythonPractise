# Challenge : Keep Only String Values & Convert Them to UPPERCASE

user = {
    'id' : 1,
    'name' : "John",
    "age" : 30,
    "city" : "Berlin"
}

# 3 Components : key value expression, a loop and and on optional condition

user_str = {
    # Expression
    # Loop
    # Filter

    k.lower():v.upper() # Expression
    for k, v in user.items() # Loop
    if isinstance(v,str) # Filter
}

print(user_str)