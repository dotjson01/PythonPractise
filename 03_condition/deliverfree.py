# use ternary operator 
# if order_amount > 300 then delivery is free else have to pay 30/- for delivery
#

# this is mannual way 
order_amount = 202
print(f"Delivery is free") if order_amount > 300 else print(f"Have to pay 30/- for delivery")

# another way 
delivery_fee = 0 if order_amount > 300 else 30
print(f"Delivery fee is {delivery_fee}")