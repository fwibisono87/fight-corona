from django.shortcuts import render, redirect
from .forms import FormPengalaman
from .models import Pengalaman
# Create your views here.


def maskermu(request):
    form_pengalaman = FormPengalaman()
    if request.method == 'POST':
        form_fix = FormPengalaman(request.POST)
        if (form_fix.is_valid()):
            pengalaman = Pengalaman()
            pengalaman.cerita_pengalaman = form_fix.cleaned_data['cerita_pengalaman']
            pengalaman.save()
        return redirect('/maskermu/listpengalaman')
    else:
        form = FormPengalaman()
        pengalaman = Pengalaman.objects.all()
        context = {
            'Form': form,
            'pengalaman': pengalaman
        }
        return render(request, 'jati/maskermu.html', context)

def listpengalaman(request) :
    pengalaman = Pengalaman.objects.all()
    return render(request, 'jati/listpengalaman.html', {'listpengalaman': pengalaman})
