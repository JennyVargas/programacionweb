from django.shortcuts import render, redirect
from django.template import loader
from .models import Producto
from .forms import ProductoForm
# Create your views here.

def Registro(request):
    Productos = Producto.objects.all()
    datos = {
        'Productos': Productos
    }
    
    return render(request, 'core/Registro.html', datos)

#aqui
def suscribete(request):
       
    
    return render(request, 'core/suscribete.html')
#aqui
def Tienda2(request):
       
    
    return render(request, 'core/Tienda2.html')
#aqui
def Tienda(request):
   
    
    return render(request, 'core/Tienda.html')

#aqui 

def principal(request):
    
    return render(request, 'core/principal.html')

def form_Producto(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"

    return render(request, 'core/form_Producto.html', datos)

def form_mod_Producto(request, id):
    producto = Producto.objects.get(SKU=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_Producto.html', datos)

def form_del_Producto(request, id):
    producto = Producto.objects.get(SKU=id)
    producto.delete()
    return redirect(to="Registro")
