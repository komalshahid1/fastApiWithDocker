import re
from wtforms import validators

def is_valid_email(email):
    try:
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(email_regex, email))
    except Exception as e:
        print(f'is_valid_email Exception: {e}')
        return False

def boolean_validator(form, field):
    if isinstance(field.data, bool):
        return
    if field.data.lower() in ('true', 'false', '1', '0'):
        field.data = field.data.lower() in ('true', '1')
        return
    raise validators.ValidationError('Field must be a boolean (true/false or 0/1)')
