import re

# check if the email is valid
def is_valid_email(email):
    if len(email) < 7:
        return False
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        return True  
    return False

# split emails from a string
def split_emails(email_string:str):
    # Define a regex pattern for matching email addresses
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    # Find all email addresses in the input string
    emails_list = re.findall(email_pattern, email_string)

    return emails_list
