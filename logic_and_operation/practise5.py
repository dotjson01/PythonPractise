# check if the user is either an admin or a moderator and either they're not banned or they've verified their email

email = "test@example.com"
user_role = "admin"
banned_users = ["user123", "spammer12"]

# 1. check if email is a string exists, and contain on @
is_email_valid = isinstance(email, str) and email is not None and "@" in email

# 2. Define roles and current user status
allowed_roles = ['admin', 'moderator']
is_authorized = user_role.strip().lower() in allowed_roles
is_banned = user_role in banned_users

# 3. Final logic : (Admin OR Mod) AND (Not Banned OR Email Verified)
if is_authorized and (not is_banned or is_email_valid):
    print("Verified Access")

else:
    print("Access Denied")

