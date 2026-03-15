# searching a phone code starting from +91
numbers = "+91-9854512410"

found = numbers.startswith("+91")
print(found)


'if another country code'
numbers = "+972312124210"
found =  numbers.startswith("+91")
print(found)