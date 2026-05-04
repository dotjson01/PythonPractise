# Representing a Single Row from a Database or API
row = {
    'id' : 101,
    'name' : 'John',
    'country' : 'DE',
    'age' : 29,
    "status" : 'active'
}

status_map = {
    '01' : "open",
    '02' : "In progress",
    '03' : "Done"
}
# use case : Mapping to Friendly Values
# Great for converting technical codes into friendly lables


country_map = {
    'DE'  : "Germany",
    'FR'  : "France",
    "IN" : "India"
}

# Storing Environment Variable & Configuration
system_co = {
    "DB_HOST" : "prod-xgxgjls.com",
    "DB_PORT"  : 5421,
    "DB_USER" : "admin-user",
    "DB_NAME" : "Analytics-dashboard"
}
# store system settings like host, port and usernmaes in one clean place
