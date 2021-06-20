from django.urls import path
from .views import home,contacto,login,registro

urlpatterns = [
    path('', home,name="home"),
    path('contacto/',contacto,name="contacto"),
    path('login/',login,name="login"),
    path('registro/',registro,name="registro")
]
