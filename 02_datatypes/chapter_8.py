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