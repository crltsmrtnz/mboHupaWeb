from django.urls import path
from usuario.views import RegistroUsuario


#from apps.usuario.views import UserAPI


urlpatterns = [
    path('registrar/', RegistroUsuario.as_view(), name='registrar'),
    #path('api/', UserAPI.as_view(), name='api'),

]
