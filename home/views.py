from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponseRedirect 
from .forms import RegistrationForm

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request,'page/register.html', {'form': form})
    

def index(request):
    return render(request, 'page/home.html')


def index1(request):
    return render(request, 'page/about.html')


def contact(request):
    return render(request, 'page/contact.html')
