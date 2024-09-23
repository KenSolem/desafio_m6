from django.http import HttpResponse
from django.shortcuts import render # se agregó para llamar las paginas web del template
from paginas.models import Flan

def home(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'flanes': flanes_publicos,
    }
    return render(request, 'home.html', context)  

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'flanes': flanes_privados,
    }
    return render(request, 'welcome.html', context)  

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


