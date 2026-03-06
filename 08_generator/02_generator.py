# how does infinite generator work and where it is useful ?
# it is useful in streams and real time system where the constant data needs to go on
# they can drain a memory 

def infinite_chai():
    count = 1 # user get a coffee first time 
    while True: # want refill again yes can be 
        yield f"Refile #{count}" # we cant to take numbers of count , user can able to refill
        count += 1 # count +1 where refilled

refill = infinite_chai() # let call it
 
for _ in  range(3): # it will run till 3 time , that means you only having 3 times to refill 
    print(next(refill))