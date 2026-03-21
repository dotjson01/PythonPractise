# check if a user's email is not empty, contain '@', and ends with '.com'

email = "abc@gmail.com"
checking = email != "" and "@" in email and email.endswith('.com')
print(checking)



email = "abcgmail.com"
checking = email != "" and "@" in email and email.endswith('.com')
print(checking)


email = "abc@gmail"
checking = email != "" and "@" in email and email.endswith('.com')
print(checking)


email = ""
checking = email != "" and "@" in email and email.endswith('.com')
print(checking)