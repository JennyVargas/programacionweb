from django import forms
from django.forms import ModelForm 
from .models import Producto

class ProductoForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = ['SKU', 'Nombre', 'Precio', 'Stock', 'Descripcion', 'Categoria',]