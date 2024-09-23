from django.http import HttpResponse
from django.shortcuts import render, redirect # se agregó para llamar las paginas web del template
from paginas.models import Flan, Contact
from paginas.forms import ContactForm

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
    if request.method == 'GET':
        form = ContactForm()
        context = {'form': form}
        return render (request, 'contact.html', context)
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                **form.cleaned_data
            )
            return redirect('/success')
        context = { 'form': form}
        return render(request, 'contact.html', context)    
        
def success(request):
    return render(request, 'success.html')



