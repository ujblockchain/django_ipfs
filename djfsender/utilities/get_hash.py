import hashlib

# finding the SHA-256 message digest of a file
# This function returns the SHA-256 hash of the byte string passed into it"""


def object_hash(object_string):
    # Calculate the hash of the read byte string
    hash_object = hashlib.sha256(object_string)
    hex_dig = hash_object.hexdigest()

    # return the hex representation of digest
    return hex_dig
