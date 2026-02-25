# first talk about pure function and impure function
# recursive
# lambdas


#  recursive

def rec(n):
    print(n)
    if n == 0:
        return "Hello"
    return rec(n-1) 

print(rec(3))


#lambdas
chai_type =["light", "kadak", "Ginger", "Masala Chai","kadak"]

strong_chai = list(filter(lambda chai: chai!="kadak",chai_type))
print(strong_chai)
# ['light', 'Ginger', 'Masala Chai']


strong_chai1 = list(filter(lambda chai: chai=="kadak", chai_type))
print(strong_chai1)
# ['kadak', 'kadak']