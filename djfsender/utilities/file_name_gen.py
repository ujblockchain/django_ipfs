import random
import string

# generate random file name


def get_random_file_name(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase

    # generate to max length
    result_str = ''.join(random.choice(letters) for i in range(length))

    # return result
    return result_str
