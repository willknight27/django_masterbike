from django.shortcuts import render

# Pagina de Inicio
def home(request):
    return render(request,'core/home.html')

def contacto(request):
    return render(request,'core/contacto.html')

def login(request):
    return render(request,'core/login.html')

def registro(request):
    return render(request,'core/registro.html')