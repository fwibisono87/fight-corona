from django.shortcuts import render, redirect
from .forms import FormKegiatan
from .models import Kegiatan
# Create your views here.


def edukasi(request):
    form_kegiatan = FormKegiatan()
    if request.method == 'POST':
        form_fix = FormKegiatan(request.POST)
        if (form_fix.is_valid()):
            kegiatan = Kegiatan()
            kegiatan.nama_kegiatan = form_fix.cleaned_data['nama_kegiatan']
            kegiatan.save()
        return redirect('/edukasi/listkegiatan')
    else:
        form = FormKegiatan()
        kegiatan = Kegiatan.objects.all()
        context = {
            'Form': form,
            'kegiatan': kegiatan
        }
        return render(request, 'farah/edukasi.html', context)

def listkegiatan(request) :
    kegiatan = Kegiatan.objects.all()
    return render(request, 'farah/listkegiatan.html', {'listkegiatan': kegiatan})
