# A local system cafe wants a program that suggests a snack . If a customer asks for a cookies or samosa it confirms the order 
# otherwise it says it's not available

# take snack input 
# if it's cookies or samosa confirms the order 
# else show unavailability 


# this is mannual way 
#  snacks = ['samosa', 'cookies']
#  if 'ginger' in snacks:
#  print(f"Yes Available ")
#  
#  else :  print(f"Sorry unavailable Can try later ")


snack = input("Enter your preferred choice : ").lower()
if snack == "samosa" or snack== "cookies" : print(f"Great Choice Thanks for confirmation {snack}")
else: print(f"Sorry item is not available ")