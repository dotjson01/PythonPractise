a= {10, 20, 30, 40, 50}
b = {30, 40, 50}

print(a.issubset(b))

a= { 30, 40, 50}
b = {30, 40, 50,60}

print(a.issubset(b))

print(b.issuperset(a))

# if b is the superset of a means b comes in a
print(b.issuperset(a))


# isdijoint() returns TRUE if both sets share no items (No Overalapping)
a = {45, 44, 5, 30}
b= {7, 66, 78}
print(a.isdisjoint(b)) # False
