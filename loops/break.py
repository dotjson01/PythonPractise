'''
we are using break loop , checking the value is empty then break it and tell user to fill first empty value
'''

names = ["john", "rohan", "raju", "", "mohan"]
for name in names:
    if name == "":
        print("Empty Invalid String")
        break
    print(f"{name}")
    