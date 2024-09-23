from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        label='Nombre:',
        widget=forms.TextInput(attrs=
            {'class': 'form-control mb-3 fst-italic', 
            'placeholder': 'Ingrese su nombre aquí'
        })
    )
    email = forms.EmailField(
        max_length=100,
        label='Email:',
        widget=forms.EmailInput(attrs=
            {'class': 'form-control mb-3 fst-italic', 
            'placeholder': 'Ingrese correo aquí'
        })
    )
    mensaje = forms.CharField(
        max_length=500,
        label='Mensaje:',
        widget=forms.Textarea(attrs=
            {'class': 'form-control mb-3 fst-italic', 
            'placeholder': 'Ingrese mensaje. Maximo 500 carácteres'
        })
    )           
                     
            
