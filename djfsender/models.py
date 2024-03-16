from django.db import models
from django.utils.timezone import datetime
from autoslug import AutoSlugField
from shortuuid.django_fields import ShortUUIDField
from .utilities.validate_files import check_file


class FileSender(models.Model):
    file_id = ShortUUIDField(
        length=10,
        max_length=13,
        prefix='',
        alphabet='21345687abcdefg1234',
        verbose_name='File Id',
        primary_key=True,
    )

    file_name = models.CharField(max_length=100, help_text='file name')
    slug = AutoSlugField(
        populate_from='file_name',
        unique_with=['file_id', 'created__second'],
    )
    file = models.FileField(validators=[check_file])
    file_hash = models.CharField(max_length=200, help_text='sha256 hash of file before upload to pinata')
    ipfs_hash = models.CharField(max_length=300)
    pin_size = models.IntegerField(help_text='size in kb', default=0)
    pin_time_stamp = models.CharField(max_length=100, help_text='time file was saved in pinata', default='')
    file_description = models.TextField(help_text='file description')
    created = models.DateTimeField(auto_now_add=True, help_text='time record was created in model')
    last_updated = models.DateTimeField(default=datetime.now(), help_text='time record was updated in model')

    def __str__(self):
        return self.file_name

    class Meta:
        ordering = ['created']
