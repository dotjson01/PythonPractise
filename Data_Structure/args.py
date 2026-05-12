# calculate the total of multiple values

'''


def total(a,b,):
    print(a+b)

total(1,2)
# it is very simple that both these values gonna pass into this args

total(1,2,3)
# now what if we are having 3 values and in next we have multiple values then does we have to change the value inside parameter again and again



'''

# To solve this problem we having

def total(*args):
    print(sum(args))

total(1,2)
total(1.2,3)
total(1,2,3,4)
total(1,2,3,4,5,6)