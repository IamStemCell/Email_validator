# Email_validator
Module validates emails for format and filters by domain (whitelist/blacklist)


#Features 
- Checks valid email format using regular expressions
- Optional **domain whitelisting** and **blacklisting**

#Usage example

```python
from email_validator import is_valid_email

email = "user@gmail.com"
result = is_valid_email(email, whitelist=["gmail.com"], blacklist=["spam.com"])
print(result)  # True
