import random
import string


def get_random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))


def get_random_value():
    return random.randint(0, 10000)


def get_formated_value(value):
    if value < 0:
        return '-${:,.2f}'.format(-value)
    else:
        return '${:,.2f}'.format(value)