#dictinory 

chai_order = dict(type="Masala", size="Medium", price="1200");
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

