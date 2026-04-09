import re

text = "My email is example@gmail.com and phone is 9876543210"

# Match email
email_pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
emails = re.findall(email_pattern, text)

# Match phone number (10 digits)
phone_pattern = r'\b\d{10}\b'
phones = re.findall(phone_pattern, text)

print("Emails found:", emails)
print("Phone numbers found:", phones)

# Search example
match = re.search(email_pattern, text)
if match:
    print("First email found:", match.group())