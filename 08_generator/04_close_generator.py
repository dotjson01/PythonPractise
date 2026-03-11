# sometimes yield and generator  generate the values then need to borrows 
def local_chai():
    yield "Masala Chai"                                                                                     # yield -> the basic purpose of yield is to pause and execution of a function , main guy converting into a generator
    yield "Ginger Chai"                                                                                     #  next() -> manually getting the next value 
def imported_chai():                                                                                        # .send -> sending data to generator
    yield "Match"                                                                                           # yield from -> getting value from another generator, sometimes delegate the tasks
    yield "Oolang"                                                                                          # close -> basically used to cleanup the memory and peacefully stop the generator

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print (chai)


    # we are using try expect 

def stall():
    try:
        order = yield "Wating for a chai"
    except:
        print( "Stall closed")


chai_stall = stall()
print(next(chai_stall))
chai_stall.close() #closing generator that is good idea to close this because due to memeory leakage save