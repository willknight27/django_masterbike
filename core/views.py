from django.shortcuts import redirect, render
from .models import Arriendo
from .forms import ArriendoForm
from django.contrib import messages


# Pagina de Inicio
def home(request):
    return render(request,'core/home.html')

def contacto(request):
    return render(request,'core/contacto.html')

def login(request):
    return render(request,'core/login.html')

def registro(request):
    return render(request,'core/registro.html')

def arriendo(request):
    arriendo = Arriendo.objects.all()
    data ={
        'arriendo': arriendo
    }
    return render(request,'core/arriendo.html',data)

def agregar_arriendo(request):
    
    data ={
        'form': ArriendoForm()
    }

    if request.method == 'POST':
        formulario = ArriendoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Bicicleta agregada correctamente")
            return redirect(to="arriendo")
        else:
            data["form"] = formulario
            messages.info(request,"Rellene los campos correctamente")
            return redirect(to="agregar-arriendo")

    return render(request, 'core/arriendo_bicicleta/agregar.html',data)
