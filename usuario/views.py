from django.shortcuts import render

# Create your views here.
#import json
#from rest_framework import APIView
#from apps.usuario.serializers import UserSerializer
from django.core import serializers


from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy


from usuario.forms import RegistroForm



class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('mascota_listar')



"""
class UserAPI(APIView):
    serializer = UserSerializer
    
    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)

        return HttpResponse(json.dumps(response.data), content_type='application/json')
"""

