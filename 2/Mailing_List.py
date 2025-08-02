def is_valid_email(email):
    email = email.strip()

    if " " in email:
        return False

    if email.count('@') != 1:
        return False

    local, domain = email.split('@')

    if not local or not domain:
        return False

    for ch in local:
        if not (ch.isalnum() or ch in ['.', '_']):
            return False

    if '..' in domain or '..' in local:
        return False

    if domain.startswith('.') or domain.endswith('.'):
        return False

    if '.' not in domain:
        return False

    domain_parts = domain.split('.')
    if any(part == '' for part in domain_parts):
        return False

    for part in domain_parts:
        if not part.isalnum():
            return False

    return True

email = "abc_user@test.in"
print(is_valid_email(email))