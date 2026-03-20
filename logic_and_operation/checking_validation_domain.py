banned_list = ["https://world.com", "https://fine.com"]

# input domain
domain = "https://example.com"

# using .strip to clean the whitespace from the right and left side
domain_checking = domain.strip().lower()

# checking 
if domain_checking not in banned_list:
    print("SAFE Website")
else:
    print("This website is dangerous for you")