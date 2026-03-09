# floating points numbers are approx presented in memory in binary form up to the allowed precision

a = 0.1+0.1+0.1 == 0.3
print(a)

# false output because cannot fully represented in binary 
print(0.1+0.1+0.1)
# see the output showing -> 0.30000000000000004