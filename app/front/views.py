from django import template
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'front/index.html')


# !! Temporary address for login page, references view and adding a reference
def login(request):
    return render(request, 'front/login.html')

def view_reference(request):
    return render(request, 'front/references.html')

def add_reference(request):
    return render(request, 'front/add_reference.html')
