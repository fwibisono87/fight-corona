from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageCreate
from django.http import HttpResponse


def index(request):
    board = Image.objects.all()
    return render(request, 'francis/index.html', {'board':board})

def upload(request):
    upload = ImageCreate()
    if request.method == "POST":
        upload = ImageCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('/forum')
        else:
            return HttpResponse("plz doublecheck ur input")
    else:
        return render(request, 'francis/upload_form.html', {'upload_form' : upload})




# Create your views here.
