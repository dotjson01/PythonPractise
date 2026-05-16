# check if a password meets the minimum length of 8

def is_valid_password (password):
    return len(password) >=8

print(is_valid_password("4514512"))
print(is_valid_password("123456789"))