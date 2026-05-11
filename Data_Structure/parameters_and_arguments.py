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
