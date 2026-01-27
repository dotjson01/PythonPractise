#dictinory 

# A Python dictionary is a data structure that stores data in key-value pairs, where each key is unique and is used to retrieve its associated value. 
# It is mainly used when you want to store and access data by a name (key) instead of by position like in a list.

chai_order = dict(type="Masala", size="Medium", price="1200");
print(f"Old Chai order {chai_order.keys()}")
print(f"Chai Order API {chai_order}");

#chai reciepe
chai_reciepe = {}
chai_reciepe['base']  = "black";
chai_reciepe['liquid'] = 'milk'
chai_reciepe['masala'] = "clove"
print(f"Chai Reciepe { chai_reciepe['base']}");
print(f"Chai Reciepe { chai_reciepe['liquid']}");

del chai_reciepe['base']
print(f"Chai Reciepe { chai_reciepe}");

chai_order = {"type" : "Masala", "size":"small", "price":"120"}
print(f"New chai order {chai_order.keys()}")
print(f"Chai Values {chai_order.values()}")
print(f"Chai order in items {chai_order.items()}")