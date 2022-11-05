from django.core.exceptions import ValidationError

def email_validator(email):
    try:
        at_idx = email.index("@")
    except ValueError:
        raise ValidationError(message="please enter a valid email address.")
    if not email[at_idx+1:] == "ualberta.ca":
        raise ValidationError(message="Please enter a ualberta email.")
    if not email[:at_idx].isalpha():
        raise ValidationError(message="please enter a valid email address.")

def password_validator(password):
    if not len(password) >= 8:
        raise ValidationError("Password must be at least 8 characters.")
    caps = 0
    for i in password:
        if i.isupper():
            caps += 1
    if not caps >= 1:
        raise ValidationError("Password must have a capital.")
