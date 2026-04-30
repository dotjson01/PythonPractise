# list comphresion

domains = ['www.google.com',
           'openai.com',  # lower case
           'localhost',
           'WWW.DATAWITHBARAA.COM' ] # upper case

cleaned =  [
    # Data Transformation
    d.lower().replace('www.', '')
    # For loop
    for d in domains 
    # Data Filtering
    if '.' in d
]

print(cleaned)