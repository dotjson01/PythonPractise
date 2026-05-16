# action Function
  # Task : store application log messages in a file on drive C

# def write_log(message):
#     with open(""):
#         file.write(message , "\n")



def is_valid_email(email):
    return "@" in email and "." in email



def clean_and_split_email(email):
    return "@" in email and "." in email

# Transformation Function

def clean_and_split_email(email):
    email = email.split().lower()
    username, domain  = email.strip("@")
    return {
        "username" : username,
        "domain" : domain
    }


# we recieve an email from a user
email = input("Please enter a email")

# we must check if it is valid
is_valid_email(email)

