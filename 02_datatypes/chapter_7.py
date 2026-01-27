#tuples ()-> Parenthesis, []-> Bracket, {} -> semi bracket or braces
# immutable
#key value pair


#    A tuple in Python is an immutable ordered collection of elements.
 #   Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
 ##   Tuples can hold elements of different data types.
 ##   The main characteristics of tuples are being ordered, heterogeneous and immutable.
 ##   Creating a Tuple
  #  A tuple is created by placing all the items inside parentheses (), separated by commas. A tuple can have any number of items and they can be of different data types.



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
