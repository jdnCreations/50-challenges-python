import sys


def check_for_palindrome(string):
    backwards_string = ""
    string = string.lower()
    for i in reversed(range(len(string))):
        backwards_string = backwards_string + string[i]

    if string != backwards_string:
        return False
    return True


if len(sys.argv) < 2:
    print('Usage: py pdc.py [text]')
    sys.exit()

print(check_for_palindrome(sys.argv[1]))
