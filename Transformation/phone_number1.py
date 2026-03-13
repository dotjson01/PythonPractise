# phone number -> +49 (179) 123-469
# convert into clean phone number

phone = "+49 (179) 123-469"
# using the concept of method chaining
print(phone.replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", ""))