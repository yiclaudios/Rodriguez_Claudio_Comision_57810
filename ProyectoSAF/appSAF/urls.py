from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('acerca/', acerca, name="acerca"),

    ## * * *  Formularios  * * *

    # PATH de CLIENTES
    path('clientes/', clientes, name="clientes"),
    path('clienteForm/', clienteForm, name="clienteForm"),
    path('clienteUpdate/<id_cliente>/', clienteUpdate, name="clienteUpdate"),
    path('clienteDelete/<id_cliente>/', clienteDelete, name="clienteDelete"),

    # PATH de VEHICULOS
    path('vehiculos/', vehiculos, name="vehiculos"),
    path('vehiculoForm/', vehiculoForm, name="vehiculoForm"),
    path('buscarVehiculos/', buscarVehiculos, name="buscarVehiculos"),
    path('encontrarVehiculos/', encontrarVehiculos, name="encontrarVehiculos"),
    path('vehiculoUpdate/<id_vehiculo>/', vehiculoUpdate, name="vehiculoUpdate"),
    path('vehiculoDelete/<id_vehiculo>/', vehiculoDelete, name="vehiculoDelete"),

    # PATH de EMPLEADOS
    path('empleados/', empleados, name="empleados"),
    path('empleadoForm/', empleadosForm, name="empleadoForm"),
    path('empleadoUpdate/<id_empleado>/', empleadoUpdate, name="empleadoUpdate"),
    path('empleadoDelete/<id_empleado>/', empleadoDelete, name="empleadoDelete"),

    # PATH de PROVEEDOR
    path('proveedorForm/', proveedoresForm, name="proveedorForm"),
    path('proveedores/', proveedores, name="proveedores"),
    path('proveedorUpdate/<id_proveedor>/', proveedorUpdate, name="proveedorUpdate"),
    path('proveedorDelete/<id_proveedor>/', proveedorDelete, name="proveedorDelete"),


    # LOGIN / LOGOUT / REGISTRACION
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),
    path('registro/', register, name="registro"),

    # EDITAR USERNAME / AVATAR
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),
]
