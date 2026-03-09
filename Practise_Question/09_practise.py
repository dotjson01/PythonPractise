# identity operator

a=10
b=10
a=b
print(a is b)
#  why true because pointing to same memory location

print(id(a), id(b))
c=40
b=c
print(b is c )
print(id(b))