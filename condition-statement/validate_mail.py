'''

Validate the Quality and Correctness of Email Values

Must not be empty
Must contain '.' and '@'
Must contain exactly one '@' symbol
Must end with '.com', '.org', or '.net'
Must not be longer than 254 characters
Must start and end with a letter or digit


'''

import re

def validate_email(email):
    """
    Validates an email based on specific business rules:
    1. Not empty
    2. Exactly one '@' and at least one '.'
    3. Ends with .com, .org, or .net
    4. Max 254 characters
    5. Starts and ends with alphanumeric characters
    """
    
    # Rule: Must not be longer than 254 characters or empty
    if not email or len(email) > 254:
        return False, "Length must be between 1 and 254 characters."

    # Pattern breakdown:
    # ^[a-zA-Z0-9]      -> Starts with a letter or digit
    # [^@]*             -> Any characters except '@'
    # @                 -> Exactly one '@' symbol
    # [^@]*             -> Any characters except '@' (the domain part)
    # \.                -> Must contain at least one '.'
    # (com|org|net)$    -> Must end with .com, .org, or .net
    # [a-zA-Z0-9]$      -> Must end with a letter or digit (inherent in com/org/net)
    
    pattern = r"^[a-zA-Z0-9][^@]*@[^@]*\.(com|org|net)$"
    
    if re.match(pattern, email, re.IGNORECASE):
        return True, "Valid Email"
    else:
        return False, "Failed validation rules (check format, '@' count, or TLD)."

# --- Testing the logic ---
test_emails = [
    "user@example.com",      # Valid
    "123@business.net",      # Valid (starts with digit)
    "@missing.org",          # Invalid (starts with @)
    "double@@point.com",     # Invalid (two @)
    "no-dot@com",            # Invalid (missing dot before TLD)
    "wrong.end@site.edu",    # Invalid (unsupported TLD)
    "a" * 255 + "@test.com"  # Invalid (too long)
]

for mail in test_emails:
    is_valid, message = validate_email(mail)
    print(f"[{'✓' if is_valid else '✗'}] {mail[:30]:<30} | {message}")
