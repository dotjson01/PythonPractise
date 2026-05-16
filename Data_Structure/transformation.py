# Task : Clean an email and split it into username and domain

def clean_and_split_email(email):
    cl_email = email.strip().lower()
    # sara@gmail.com
    username, domain = cl_email.split("@")
    return {"username": username,
            "domain": domain}


cl = clean_and_split_email("SARA@Gmail.com")
print(cl)
