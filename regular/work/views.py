from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm
import re

def index(request):
    submitbutton = request.POST.get('submit')

    regexp = ''
    lining = ''
    regularexpress = ''

    form = UserForm(request.POST or None)
    if  form.is_valid():
        lining = form.cleaned_data.get('line')
        regularexpress = form.cleaned_data.get('regular_express')
        if submitbutton == 're.search':
            regexp = re.search(regularexpress,lining)
        elif submitbutton == 're.match':
            regexp = re.match(regularexpress,lining)
        elif submitbutton == 're.findall':
            regexp = re.findall(regularexpress,lining)
        else:
            regexp = re.split(regularexpress,lining)


    context = {
        'form': form, 'lining': lining, 'regularexpress': regularexpress, 'submitbutton': submitbutton,'regexp':regexp,
    }

    return render(request,'work/index.html',context)