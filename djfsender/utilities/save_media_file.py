from django.conf import settings

# media path
media_folder = f'{settings.MEDIA_ROOT}'


# upload file to media root in chunks
def file_to_media_root(file, file_name, file_extension):
    with open(f'{media_folder}/{file_name}.{file_extension}', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
