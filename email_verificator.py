"""
email_varificator.py

A lightweight Python module for validating email addresses by format and domain.
"""

import re


def is_valid_email(email: str, whitelist: list = None, blacklist: list = None) -> bool:
    """
    Validates an email address using regex and optional domain filters.

    Args:
        email (str): The email address to validate.
        whitelist (list, optional): List of allowed domain names.
        blacklist (list, optional): List of disallowed domain names.

    Returns:
        bool: True if the email is valid and meets domain criteria, else False.
    """
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if not re.match(email_regex, email):
        return False

    try:
        domain = email.split('@')[1].lower()
    except IndexError:
        return False

    if whitelist and domain not in map(str.lower, whitelist):
        return False

    if blacklist and domain in map(str.lower, blacklist):
        return False

    return True
  
