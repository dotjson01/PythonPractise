# parametes -> Functions Definition, PlaceHolder, defines what function expects
# Arguments -> Function Call, Value (Fills Placeholder), Provides Functions with values


def greet(name):
    print("Hello " + name, 'Welcome to Community How can I help you')

call = greet('Raju')


def clean_name():
    name = " MaMria"
    print(name.strip().lower())
    print(name.strip().upper())

clean_name()
clean_name()
clean_name()


def clean_name(name):
    cleaned = name.strip().lower()
    print("RAW DATA:", name)
    print("Cleaned DATA:", cleaned)

clean_name(" MariA ")
clean_name("KUMAR")


case_rule = "n/a" #global variable
def clean_name(name):
    cleaned = name.strip()
    if case_rule == "lower":
        cleaner = cleaned.lower()
        print(cleaner)
clean_name("RAHUL")



# Building FULL Clean Name
def clean_name(first_name, last_name):
    first = first_name.strip().lower()
    second = last_name.strip().lower()
    full_name = first + " " + second
    print(full_name)

clean_name("MARIA", "KUMARI") # this is called positional arguments which means mapping the values to above function with [ first_name, last_name ]
# Here is Risky to do this thing
clean_name("KUMARI", "MARIA")

clean_name(last_name="KU",first_name="MARIGOLD")