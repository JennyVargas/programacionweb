from django.urls import path
from .views import principal, form_Producto, form_mod_Producto, form_del_Producto, Tienda, Tienda2, suscribete, Registro

urlpatterns = [
    path('', principal, name="principal"),
    path('form-Producto', form_Producto, name="form_Producto"),
    path('form-mod-Producto/<id>', form_mod_Producto, name="form_mod_Producto"),
     path('form-del-Producto/<id>', form_del_Producto, name="form_del_Producto"),
    path('Tienda', Tienda, name="Tienda"),
    path('Tienda2', Tienda2, name="Tienda2"),
    path('suscribete', suscribete, name="suscribete"),
    path('Registro', Registro, name="Registro"),
    
]
