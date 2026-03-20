# check if the password is at least 8 character long and does not contain spaces

password = "!@#@dflskhdfoshd#$$^$%&^$"
space = None
if len(password) <= 8 and space != " ":
    print("Password Invalid")
else:
    print("Password is Correct")




password = " "
space = None
if len(password) <= 8 and space != " ":
    print("Password Invalid")
else:
    print("Password is Correct")