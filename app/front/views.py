from django import template
from django.shortcuts import render

# Create your views here.
from refs.models import Ref
from refs.forms import RefForm

from django import forms
#from django.forms import RefForm
from .forms import ReferenceForm

def index(request):
    return render(request, 'front/index.html')


# !! Temporary address for login page, references view and adding a reference
def login(request):
    return render(request, 'front/login.html')

def view_reference(request):
    # return render(request, 'refs/refs-list.html')
    return render(request, 'front/references.html')



# def add_reference(request):
#     if request.method == 'POST':
#         form = ReferenceForm(request.POST)
#     else:
#         form = ReferenceForm
#     return render(request, 'front/add_reference.html', {'form': form})


def refs_add(request):
    if request.method == 'POST':
        form = RefForm(request.POST)
    else:
        form = RefForm
    return render(request, 'front/refs_add.html', {'form': form})