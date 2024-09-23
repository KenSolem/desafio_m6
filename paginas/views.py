from django.http import HttpResponse
from django.shortcuts import render # se agregó para llamar las paginas web del template

def home(request):
    return render(request, 'paginas/home.html')  

def about(request):
    return render(request, 'paginas/about.html')

def contact(request):
    return render(request, 'paginas/contact.html')
