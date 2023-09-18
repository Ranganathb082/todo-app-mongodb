import re
import passlib.pwd

def validate_username(username):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{5,}$"
    match = re.match(pattern, username)
    return bool(match)

def validate_password(password):
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@_]).{8,}$"
    match = re.match(pattern, password)
    return bool(match)