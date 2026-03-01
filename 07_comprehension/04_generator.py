# generator are used to saving the memory
#  (expression for item in iterable if condition)

daily_sales = [100, 150, 200, 250, 300]

# i want to get sum of all the sales
total_sales = sum(sale for sale in daily_sales if sale>100)
print(f"Total Sales : {total_sales}")