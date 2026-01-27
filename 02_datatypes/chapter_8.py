# mutable -> list

ingredients = ["water", "milk", "black tea"];
#append -> adding sugar at last
ingredients.append("sugar");
print(f"{ingredients}")
#remove -> removing water word if anywhere present
ingredients.remove("water");
print(f"{ingredients}")

spice_option = ["Ginger", "Cadamon"]
chai_ingredients = ["water", "tea bag"]

#extend -> extending list to another list 
spice_option.extend(chai_ingredients);
print(f"Extended {spice_option}");

#insert something at some particular space
spice_option.insert(2, "white powder");
print(f"Inserted White powder into it : {spice_option}");

#pop something -> but only from end
spice_option.pop(2)
print(f"White powder poped up and left with -> {spice_option}")

#reverse
spice_option.reverse()
print(f"Reversed Spice {spice_option}")


#sort
spice_option.sort()
print(f"Sorted {spice_option}")

#find max and min
sugar_level = 1, 2 ,3, 4
print(f"Suagr level Max {max(sugar_level)}");
print(f"Suagr level Min {min(sugar_level)}");

#operator overloading ( + ) -> adding whole variable to another variable
liquid_mix = ["milk", "golla", "Jeera"];
base_mix = ["soda", "paani", "lassi"];
full_mix=  liquid_mix + base_mix;
print(f"Full Mix {full_mix}")


#operator overlaoding ( * ) ->  multiplying with each element
strong_brew = ["water", "jeera"] * 3;
print(f"Strong Brew { strong_brew}")

#modifying list from a particular word like CIRRAMON -> CARDMON
store_variable = bytearray(b"CIRRAMON")
store_variable = store_variable.replace(b"CIRRA", b"CARD");
print(f"Store Variable change froom {store_variable}");