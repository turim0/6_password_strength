import re
from collections import Counter
import argparse
import sys
import os


def includes_case_sensivity(password):
    return bool(re.search(r'[a-z][A-Z]', password))


def includes_digits(password):
    return bool(re.search(r'\d', password))


def length_quality(password):
    return sum([len(password) > 5, len(password) > 8, len(password) > 15])


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


def load_data(file_path):
    with open(file_path, encoding='utf8') as file:
        return file.read()


def is_in_blacklist(password, blacklist):
    return blacklist.find(password) != -1


def get_password_strength(password, blacklist):
    return (sum([1,
                 includes_case_sensivity(password),
                 includes_digits(password),
                 length_quality(password),
                 includes_special_symbols(password),
                 is_diverse(password),
                 not is_banned_by_mask(password),
                 not is_in_blacklist(password, blacklist)]
                )
            )


if __name__ == '__main__':
    file_path = sys.argv[1] if len(sys.argv) > 1 else None
    if file_path is None:
        sys.exit('Usage: password_strength.py + password blacklist file')
    if not os.path.isfile(file_path):
        sys.exit('Please pass correct file name')
    password = input('Input password: ')
    blacklist = load_data(file_path)
    strength = get_password_strength(password, blacklist)
    print('Password strength: {}'.format(strength))

