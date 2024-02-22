import json
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponsePermanentRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView


from .service import FileSenderService
from .forms import FileSenderForm
from .models import FileSender


class HomeView(SuccessMessageMixin, CreateView):
    form_class = FileSenderForm
    success_message = "File %(file_name)s uploaded successfully"
    model = FileSender
    template_name = 'index.html'

    def form_valid(self, form):
        # init file name
        file_name = ''
        file_stream_hash = ''
        check_if_hash_exist = ''
        # save file to media root

        # if not FileSenderService.check_hash_exist("5774h74")
        for field in self.request.FILES.keys():
            for formfile in self.request.FILES.getlist(field):
                # check if the file hash already exits
                # init file hash using incoming byte string
                file_stream_hash = FileSenderService.get_object_hash(formfile.read())
                check_if_hash_exist = FileSenderService.check_hash_exist(
                    file_stream_hash
                )

        # only save file if hash does not exist
        if not check_if_hash_exist:
            # set file name
            file_name = FileSenderService.get_file_name()
            FileSenderService.upload_to_media_root(formfile, file_name)

            # set file path
            file_path = f'{settings.MEDIA_ROOT}/{file_name}.png'
            # Upload file to ipfs
            file = FileSenderService.ipfs_pin_file(file_name, file_path)
            # convert json to dict
            file_dict_response = json.loads(file)

            # save model
            FileSenderService.create_file_sender(
                file_name,
                file_path,
                file_stream_hash,
                file_dict_response['IpfsHash'],
                file_dict_response['PinSize'],
                form.cleaned_data['file_description'],
                file_dict_response['Timestamp'],
            )

        # redirect to view page
        return HttpResponsePermanentRedirect(
            reverse(
                'file_details',
                kwargs={'file_id': FileSenderService.get_file_id(file_stream_hash)},
            )
        )

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_object(form=form))


class FileDetails(DetailView):
    model = FileSender
    queryset = FileSender.objects.all()
    template_name = 'form-detail.html'
    context_object_name = 'file'
    pk_url_kwarg = 'file_id'

    def get_queryset(self):
        # get file id
        id = self.kwargs.get('file_id')

        # return updated querysets
        return FileSenderService.get_file_details(id)
