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
        regexp = re.search(regularexpress,lining)

    context = {
        'form': form, 'lining': lining, 'regularexpress': regularexpress, 'submitbutton': submitbutton,'regexp':regexp,
    }
    return render(request,'work/index.html',context)