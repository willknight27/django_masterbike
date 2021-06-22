from django.urls import path
from .views import home,contacto,login,registro,arriendo,agregar_arriendo

urlpatterns = [
    path('', home,name="home"),
    path('contacto/',contacto,name="contacto"),
    path('login/',login,name="login"),
    path('registro/',registro,name="registro"),
    path('arriendo/',arriendo,name="arriendo"),
    path('agregar-arriendo/',agregar_arriendo,name="agregar-arriendo"),
]
