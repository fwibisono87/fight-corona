from django import forms


class FormPengalaman(forms.Form):
    cerita_pengalaman = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'tulis disini',
                'type': 'text',
                'required': True
            }))
