# turn the messy data into clean 
"968-Maria, (D@ta Engineer ) ;; 27y   "

' Clean the string '
'name : maria | role : data engineer | age : 27 '

str = "968-Maria, (D@t@ Engineer) ;; 27y   "

name = str.split("-")[1].split(",")[0].strip().lower()
'''
str.split("-")

  Result: ['968', 'Maria, (D@t@ Engineer) ;; 27y   ']
  (splits by "-", creates a list with 2 elements)

  
[1]
  Result: 'Maria, (D@t@ Engineer) ;; 27y   '
  (gets index 1, which is the 2nd element)


.split(",")
  Result: ['Maria', ' (D@t@ Engineer) ;; 27y   ']
  (splits that string by ",", creates a new list)

[0]
  Result: 'Maria'
  (gets index 0, which is the 1st element of the new list)


"968-Maria, (D@t@ Engineer) ;; 27y   "
            ↓
split("-") → ['968', 'Maria, (D@t@ Engineer) ;; 27y   ']
               [0]    [1] ← we want this
                    ↓
            split(",") → ['Maria', ' (D@t@ Engineer) ;; 27y   ']
                         [0] ← we want this
                         ↓
                        'Maria'

'''

role = str.split("(")[1].split(")")[0].replace("@","a").lower()
age = str.split(";;")[1].strip().replace("y", "").strip()


output = f"name : {name} | role: {role} : age : {age}"
print(output)