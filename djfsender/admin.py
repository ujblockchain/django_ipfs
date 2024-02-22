from django.contrib import admin
from .models import FileSender


class SendFileAdmin(admin.ModelAdmin):
    list_display = [
        'file_id',
        'file_name',
        'file_hash',
        'ipfs_hash',
        'pin_size',
        'pin_time_stamp',
        'last_updated',
    ]
    list_display_links = [
        'file_id',
        'file_name',
        'file_hash',
        'ipfs_hash',
        'pin_size',
        'pin_time_stamp',
        'last_updated',
    ]
    search_fields = [
        'file_id',
        'file_name',
        'file_hash',
        'ipfs_hash',
        'pin_size',
        'pin_time_stamp',
        'last_updated',
    ]
    list_per_page = 50
    show_full_result_count = True
    actions_on_top = True
    actions_on_bottom = True
    save_as_continue = True
    save_on_top = True
    fields = [
        'file_id',
        'file_name',
        'file_hash',
        'ipfs_hash',
        'pin_size',
        'pin_time_stamp',
        'file',
        'file_description',
        'last_updated',
    ]


# register models
admin.site.register(FileSender, SendFileAdmin)
