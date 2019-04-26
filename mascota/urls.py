from django.urls import path  
from django.conf.urls import url, include
from .views import listado, index_mascota, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList, \
    MascotaCreate, MascotaUpdate, MascotaDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path('', index_mascota, name='mascota'),   

    path('nueva/', login_required(MascotaCreate.as_view()), name='mascota_crear'),

    path('listar/', login_required(MascotaList.as_view()), name='mascota_listar'),

    path('editar/<pk>/', login_required(MascotaUpdate.as_view()), name='mascota_editar'),

    path('eliminar/<pk>/', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),

    path('listado/', login_required(listado), name='listado'),


]

