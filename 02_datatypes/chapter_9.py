#set -> unique
#intersection
#union

essential_spice = {"cinnamon", "cardmon", "ginger", "water"} 
optional_spice = {"cloves", "black pepper", "ginger", "water"} 
all_spice = essential_spice | optional_spice # it will gonna find union ones
print(f"All Spice {all_spice}")

#let's find the common spice both coming in essential_spice and optional_spice
common_spice = essential_spice &  optional_spice
print(f"Common Spice { common_spice}")

#finding only
only_in = essential_spice - optional_spice;
print(f"Only in {only_in}");
#checking the cloves word in a essential_spice variable
print(f"Is cloves there in essential_spice variable {'cloves' in essential_spice}")
print(f"Is cloves there in optional_spice {'cloves' in optional_spice}")