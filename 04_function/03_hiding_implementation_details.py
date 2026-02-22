# you are building a simple aap that register users
# you want to seperate concerns : getting input, validating it and saving it 
# write register_user() that calls : 
# get_input()
# validate_input()
# save_to_db()


def get_input() :
    print(f"Taking Input")

def validate_input() :
    print(f"Validating the input")

def save_to_db():
    print(f"Saved the database")


def register_user():
    get_input()
    validate_input()
    save_to_db()

register_user()
