a= {10, 20, 3, 55, 70}
b= {30, 20, 3, 78}

print (a.union(b))
# use can use | 
print(a | b)

print (a.intersection(b))
print ( a.difference(b) )
print (b.difference(a))

print(a-b)
print(b-a)
print(a.symmetric_difference(b))
