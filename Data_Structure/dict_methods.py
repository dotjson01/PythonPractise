# 
user = {'id':  1, 'age':45, 'class':'A'}
print(user)
 # print(user['name']) # it will throw error if keyword not found yet
# but if you want that not to throw error, sliently return NONE like that use .get()

print(user.get('name'))
# you can also use 

print(user['id'])

# in Operator -> Checks or tests if the key is inside the dictionary
print('age' in user) # True
print('name' in user) # False

# View Objects
print(user.keys())
print(user.values())
print(user.items())


# for Looping 
for key, value in user.items():
    print(key, value)


# add / remove / Update

user.update({'age:' : 45, "city": "Lucknow"})
print(user)

user.popitem() # popitem -> return and deletes the most recent key value pair from the dictionary
print(user)

user1 = {
    'name': None,
    'id' : None,
    'age' : None,
    'city' :None
}
user1 = dict.fromkeys([
    'id',
    'name',
    'age',
    'city'
], None ) # builds a new dictionary where all keys get the same default value
print(user1)
user1['age'] = 40 
print(user1)