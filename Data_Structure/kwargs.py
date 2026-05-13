def details(**kwargs):
    print(kwargs)

details(name="Sahil", email = "@gmail", age = 45, indian = True)

# ** When to use ** 
# Different type of values


def create_user(**kwargs):
    print(type(kwargs))
    print(kwargs)


create_user(first_name = "Mo",
            last_name = "sahil",
            age=33,
            country = "Egypt")