from django.contrib import admin

#Importando la tabla productos
from .models import Productos

#Agregando al Administrador
admin.site.register(Productos)
