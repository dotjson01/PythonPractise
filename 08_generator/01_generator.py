#  concept behind ->>>>

# you save your memory
# lazy evaluation
# you don't the result immediately 
# in the generator concept you use yield (keyword) --> one value at a time


def serve_chai():
    yield "Cup 1 : Masala Cup"
    yield "Cup 2 : Ginger Cup"
    yield "Cup 3 : Cardmom Cup"

stall = serve_chai()

for cup in stall : 
    print(cup)

def get_chai_list():
    yield "Cup1"
    yield "Cup2"
    yield "Cup3"

stall2 = get_chai_list()
print(next(stall2))
# working with this 