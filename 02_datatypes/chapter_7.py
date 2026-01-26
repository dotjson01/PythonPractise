#tuples ()-> Parenthesis, []-> Bracket, {} -> semi bracket or braces
# immutable

masala_spices = ("cadamon", "clove", "cinnamon");
(spice1, spice2, spice3) = masala_spices
print(f"masala_spices: -> {spice1}, {spice2}, {spice3}")


#swapping the values 
ginger_ratio, cadamon_ratio = 2, 1
print(f"Ginger Ratio {ginger_ratio} and Cadamon Ratio {cadamon_ratio}")
ginger_ratio, cadamon_ratio = cadamon_ratio, ginger_ratio
print(f"Swapping the values: Ginger Ratio {ginger_ratio} Cadamon Ratio {cadamon_ratio}")

#membership checking 
print(f"Is Ginger present in Spices ? {'Ginger' in masala_spices}");
print(f"Is Cadamon present ? {'cadamon' in masala_spices}"); # true if Cadamon is there it will gonna show false because of case-sensitive
