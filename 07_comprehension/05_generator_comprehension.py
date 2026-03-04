# entirely for saving the memory
# ( expression for item in iterable if condition )

daily_sales = [5, 12, 45, 8, 9, 15]
# calculate sales above 5 
# total_cups = () # this is generator comprehension
total_cups = ( sale for sale in daily_sales if sale > 5 )
print(total_cups)

# this is showing an output 
# <generator object <genexpr> at 0x72959f3ee0c0>
# why because of this -> ( )  that consume and reflect back what you want, not entirely show like list  

total_cups = sum( sale for sale in daily_sales if sale > 5 )
print(total_cups)
# the sum is giving one by one not like list -> through one by one