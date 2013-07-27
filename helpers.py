import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """
    Taken from Stack Exchange:
    http://stackoverflow.com/questions/2257441/python-random-string-generation-with-upper-case-letters-and-digits
    """
    return ''.join(random.choice(chars) for x in range(size))
