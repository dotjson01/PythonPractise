# a tea stall offers different prices for different sizes 
# write a program that calculates the price based on size

# input : "small" "medium" "large"
# small -> $10,  medium $14 large $15 
# invalid show "unknown cup size"

cupsize = input("Enter the cup size you want -> ").lower()
if cupsize == "small" : print(f"Cost for small cup is $10")
elif cupsize == "medium" : print(f"Cost for mediium cup is $14")
elif cupsize == "laege" :  print(f"Cost of large cup is $15")
else : print(f"Invalid cup size ");