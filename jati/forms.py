from django import forms


class FormKegiatan(forms.Form):
    nama_kegiatan = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'tulis disini',
                'type': 'text',
                'required': True
            }))
