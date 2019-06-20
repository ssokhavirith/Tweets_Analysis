import string


def remove_special_chars(my_string):
    whitelist = string.letters + string.digits + ' '
    new_my_string = ''.join(c for c in my_string if c in whitelist)
    return new_my_string
