import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def is_valid_email(email):
    if not isinstance(email, str):
        return False
    return bool(EMAIL_RE.match(email))
