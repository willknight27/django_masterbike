from django.contrib import admin
from .models import Arriendo, Bicicleta, Marca_Bicicleta, Tipo_Bicicleta

admin.site.register(Arriendo)
admin.site.register(Bicicleta)
admin.site.register(Marca_Bicicleta)
admin.site.register(Tipo_Bicicleta)
