#! /usr/bin/env

"""Caesar cipher and helper functions to find a CTF flag."""

import os
import re
import string
import sys


def simple_caesar(txt, rot=7):
    """Caesar cipher through ASCII manipulation, lowercase only."""
    alphabet = string.ascii_lowercase                   # pick alphabet
    shifted_alphabet = alphabet[rot:] + alphabet[:rot]  # shift it
    table = str.maketrans(alphabet, shifted_alphabet)   # create mapping table
    return txt.lower().translate(table)                 # apply


def caesar(txt, rot=7):
    """Caesar Cipher through ASCII manipulation.

    Based on https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python/54590077#54590077
    """
    if rot % 26 == 0:
        # Do nothing for rot0
        return txt

    def rot_alphabet(alphabet):
        return alphabet[rot:] + alphabet[:rot]

    # create alphabet (upper and lower case ASCII) by roting independently
    alphabets = (string.ascii_lowercase, string.ascii_uppercase)
    shifted_alphabets = tuple(map(rot_alphabet, alphabets))

    # combine alphabets
    joined_alphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)

    # map the translate and apply
    table = str.maketrans(joined_alphabets, joined_shifted_alphabets)
    return txt.translate(table)


def get_flag(txt):
    """Return anything matching basic flag format, otherwise empty string."""
    flag = ""
    pattern = r'.*([a-zA-Z]{3}\{.*\}).*'   # 3 letters followed by text in {}
    m = re.match(pattern, txt)
    if m:
        flag = m.group(1)
    return flag


def brute_force(txt):
    """Brute force through Caesar ciphers looking for a flag match."""
    flag = get_flag(txt)    # Try pull a flag
    if not flag:            # If no ciphered flag, don't bother.
        return None

    txt = flag              # Only deal with the flag
    for i in range(26):
        flag = caesar(txt, i)           # Rot the text
        if flag[:3].lower() == "ctf":   # If matches the flag pattern
            return flag
    return None


def parse_file(file_path):
    """Take file_path and brute force contents for a Caesar ciphered flag."""
    with open(file_path, 'r') as f:
        for line in f:
            flag = get_flag(line)
            if flag:                        # If found flag lookalike
                flag = brute_force(flag)
                if flag:                    # If cracked the cipher
                    sys.stdout.write(flag)
                    return True

    sys.stderr.write('ERROR: No flag found!\n')
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write('ERROR: Missing file arg\n')
        sys.exit(1)

    src_file = sys.argv[1]
    if not os.path.exists(src_file):
        sys.stderr.write('ERROR: sys.argv[1] was not found!\n')
        sys.exit(1)

    parse_file(src_file)
