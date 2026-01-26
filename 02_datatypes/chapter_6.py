#string
# in the string we are gonna see -> Core String, Indexing, Slicing
# string is immutable

chai_type = " Ginger"
customer_name = "Priya"
print(f"Order for {customer_name} : {chai_type} Please ! ")

#indexing
chai_description = "Masala with Kadak Chai"
print(f"Printing First Word {chai_description[0:6]}")
print(f"Last Word {chai_description[6:]}")

#if you want reverse a string 
print(f"Reversing a string {chai_description[::-1]}")

#encoding and decoding 
label_name = "This is the Secret message from Dark Market"
encode_name = label_name.encode("utf-16")
print(f"Label Name : {label_name}");
print(f"Encode Name : { encode_name}");
decode_name = encode_name.decode("utf-16");
print(f"Decoded Message : {decode_name}")
