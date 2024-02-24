import os
from django.core.exceptions import ValidationError

# ensure file upload do not exceed 400kb


def check_file(value):
    # check file size
    filesize = value.size

    # ensure size does not exceed 400kb
    if filesize > 409610:
        raise ValidationError('Maximum file size that can be uploaded is 400kb')
    else:
        return value
