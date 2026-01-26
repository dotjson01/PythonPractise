# this is immutable code
small_mix = 12;
print(f"Initial Value of small mix id: {id(small_mix)}");
small_mix = 45;
print(f"Second Value of small mix id : {id(small_mix)}");
# this only showing memory 


small_mix = 13;
print(f"Initial Value of small mix id: {(small_mix)}");
small_mix = 46;
print(f"Second Value of small mix id : {(small_mix)}");
# this is showing values

# this is showing values of second one's value
print(f"Initial Value of small mix id: {id(small_mix)}");
print(f"Second Value of small mix id : {id(small_mix)}");