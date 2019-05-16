from .forms import UserCreationFormWhitWmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

# Create your views here.
class SignupView(CreateView):
    form_class = UserCreationFormWhitWmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


    #Creamos mensaje de exito de inicio de sesion
    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignupView, self).get_form()
        
        #Modificacio del formulario en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Direccion de email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la Contraseña'})
        return form

