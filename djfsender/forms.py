from django import forms
from .models import FileSender
from .utilities.validate_files import check_file


class FileSenderForm(forms.ModelForm):
    file_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form__field', 'placeholder': 'File Name'}
        )
    )

    file = forms.FileField(
        validators=[check_file],
        widget=forms.FileInput(attrs={'class': 'account-setting__avatar'}),
    )

    file_description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form__field form__field--textarea',
                'placeholder': 'File Description',
                'cols': '10',
                'rows': '8',
            }
        )
    )

    class Meta:
        model = FileSender
        fields = ['file_name', 'file', 'file_description']
