from .utilities.file_name_gen import get_random_file_name
from .utilities.ipfs import pin_file
from .utilities.save_media_file import file_to_media_root
from .utilities.get_hash import object_hash
from .models import FileSender


class FileSenderService:

    @staticmethod
    def get_file_name():
        return get_random_file_name(16)

    @staticmethod
    def upload_to_media_root(file, file_name, file_extension):
        file_to_media_root(file, file_name, file_extension)

    @staticmethod
    def get_object_hash(object_string):
        return object_hash(object_string)

    @staticmethod
    def ipfs_pin_file(file_name, file_path):
        return pin_file(file_name, file_path)

    @staticmethod
    def check_hash_exist(upload_file_hash):
        # check if the hash already exist
        return FileSender.objects.filter(file_hash=upload_file_hash).exists()

    @staticmethod
    def create_file_sender(
        file_name,
        file_path,
        file_hash,
        ipfs_hash,
        pin_size,
        file_description,
        time_stamp,
    ):
        FileSender.objects.create(
            file_name=file_name,
            file_hash=file_hash,
            file=file_path,
            ipfs_hash=ipfs_hash,
            pin_size=pin_size,
            pin_time_stamp=time_stamp,
            file_description=file_description,
        )

    @staticmethod
    def get_file_id(file_hash):
        return FileSender.objects.get(file_hash=file_hash).file_id

    @staticmethod
    def get_file_details(file_id):
        return FileSender.objects.filter(file_id=file_id)
