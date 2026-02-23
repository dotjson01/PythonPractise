# your shop adds a 10% VAT on every order
# your want it to be consistent and traceable
# write add_vat(price, vat_price)
# use it to compute final prices for 3 orders

def vat(price, vat_price):
    return print(f"{price + (100+vat_price)/100 }")


orders = [100, 425, 652]

for price in orders: 
    final_amount = vat(price, 10)
    print(f"{final_amount}")

