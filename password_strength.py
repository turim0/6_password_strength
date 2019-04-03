import re
from collections import Counter
import sys
import os
import getpass


def contains_uppercase_and_lowercase_letters(password):
    return password.islower()==password.isupper()


def includes_digits(password):
    return bool(re.search(r'\d', password))


def get_length_quality(password):
    normal_length = 5
    good_length = 8
    perfect_length = 15
    return sum([
        len(password) > normal_length,
        len(password) > good_length,
        len(password) > perfect_length
    ])


def includes_special_symbols(password):
    return bool(re.search(r'[^a-zA-Z0-9]', password))


def is_diverse(password):
    return len(Counter(password).keys()) > 6


def is_banned_by_mask(password):
    patterns = [
        #phones
        r'^((8|\+7)[\-]?)?(\(?\d{3}\)?[\-]?)?[\d\-]{7,10}$',
        #dates
        #DD/MM/YYYY
        r'(0?[1-9]|[12][0-9]|3[01])[-/.](0?[1-9]|1[012])[-/.](19|20)\d\d',
        #YYYY-MM-DD
        r'[0-9]{4}[-/.](0?[1-9]|1[012])[-/.](0?[1-9]|1[0-9]|2[0-9]|3[01])'
    ]
    return any(re.search(pattern, password) for pattern in patterns)


def load_blacklist(file_path):
    with open(file_path, encoding='utf8') as file:
        return file.read().splitlines()


def is_in_blacklist(password, blacklist):
    return password in blacklist


def get_password_strength(password, blacklist):
    return sum([
        1,
        contains_uppercase_and_lowercase_letters(password),
        includes_digits(password),
        get_length_quality(password),
        includes_special_symbols(password),
        is_diverse(password),
        not is_banned_by_mask(password),
        not is_in_blacklist(password, blacklist)
    ])


if __name__ == '__main__':
    file_path = sys.argv[1] if len(sys.argv) > 1 else None
    if file_path is not None:
        if not os.path.isfile(file_path):
            sys.exit('Please pass correct file name')
        blacklist = load_blacklist(file_path)
    else:
        print('Warning: use password blacklist file to check your password')
        print('Usage:python password_strength.py + path to your file')
        blacklist = []
    password = getpass.getpass('Password: ')
    strength = get_password_strength(password, blacklist)
    print('Password strength: {}'.format(strength))

