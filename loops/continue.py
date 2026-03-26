'''
we are using continue loop , checking the value is empty then skip that loop 
'''

names = ["john", "rohan", "raju", "", "mohan"]
for name in names:
    if name == "":
        print("Empty Invalid String")
        continue
    print(f"{name}")
    