from .views import *
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

# Esto es para qie se obligue que el usuario esté logueado
from django.contrib.auth.mixins import LoginRequiredMixin # Esto trabaja sobre las clases
from django.contrib.auth.decorators import login_required # Esto trabaja sobre las funciones

def home(request):
    return(render(request, "entidades/index.html"))

@login_required
def vehiculos(request):
    contexto = {"vehiculos" : Vehiculo.objects.all()}
    return(render(request, "entidades/vehiculos.html", contexto))

@login_required
def proveedores(request):
    contexto = {"proveedores" : Proveedor.objects.all()}
    return(render(request, "entidades/proveedores.html", contexto))

@login_required
def clientes(request):
    contexto = {"clientes" : Cliente.objects.all()}
    return(render(request, "entidades/clientes.html", contexto))

@login_required
def empleados(request):
    contexto = {"empleados" : Empleado.objects.all()}
    return(render(request, "entidades/empleados.html", contexto))

@login_required
def acerca(request):
    return(render(request, "entidades/acerca.html"))

#******************************
# * * *    Formularios    * * *
#******************************

# *******   CLIENTES    *******

@login_required
def clienteForm(request):
    if (request.method == "POST"):
        miForm = ClienteForm(request.POST)
        if (miForm.is_valid()):
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_email = miForm.cleaned_data.get("email")
            cliente = Cliente(nombre = cliente_nombre, apellido = cliente_apellido, email = cliente_email)
            cliente.save()
            contexto = {"clientes" : Cliente.objects.all()}
            return(render(request, "entidades/clientes.html", contexto))
    else:
        miForm = ClienteForm()
    
    return(render(request, "entidades/clienteForm.html", {"form" : miForm}))
# -- - --
@login_required
def clienteUpdate(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente.nombre = miForm.cleaned_data.get("nombre")
            cliente.apellido = miForm.cleaned_data.get("apellido")
            cliente.email = miForm.cleaned_data.get("email")
            cliente.save()
            contexto = {"clientes" : Cliente.objects.all()}
            return(render(request, "entidades/clientes.html", contexto))
    else:
        miForm = ClienteForm(initial={"nombre" : cliente.nombre, 
                                       "apellido" : cliente.apellido, 
                                       "email" : cliente.email}) 
    
    return(render(request, "entidades/clienteForm.html", {"form" : miForm}))
# -- - --
@login_required
def clienteDelete(request, id_cliente):
    clienteForm = Cliente.objects.get(id=id_cliente)
    clienteForm.delete()
    contexto = {"clientes" : Cliente.objects.all()}
    return(render(request, "entidades/clientes.html", contexto))

# *******  FIN CLIENTES   *******

# *******    VEHICULOS    *******

@login_required
def vehiculoForm(request):
    if (request.method == "POST"):
        miform = VehiculoForm(request.POST)
        if (miform.is_valid()):
            vehiculo_marca = miform.cleaned_data.get("marca")
            vehiculo_modelo = miform.cleaned_data.get("modelo")
            vehiculo_matricula = miform.cleaned_data.get("matricula")
            vehiculo = Vehiculo(marca = vehiculo_marca, modelo = vehiculo_modelo, matricula = vehiculo_matricula)
            vehiculo.save()
            contexto = {"vehiculos" : Vehiculo.objects.all()}
            return(render(request, "entidades/vehiculos.html", contexto))
    else:
        miform = VehiculoForm()
    
    return(render(request, "entidades/vehiculoForm.html", {"form" : miform}))
# -- - --
@login_required
def vehiculoUpdate(request, id_vehiculo):
    vehiculo = Vehiculo.objects.get(id=id_vehiculo)
    if request.method == "POST":
        miForm = VehiculoForm(request.POST)
        if miForm.is_valid():
            vehiculo.marca = miForm.cleaned_data.get("marca")
            vehiculo.modelo = miForm.cleaned_data.get("modelo")
            vehiculo.matricula = miForm.cleaned_data.get("matricula")
            vehiculo.save()
            contexto = {"vehiculos" : Vehiculo.objects.all()}
            return(render(request, "entidades/vehiculos.html", contexto))
    else:
        miForm = VehiculoForm(initial={"marca" : vehiculo.marca, 
                                       "modelo" : vehiculo.modelo, 
                                       "matricula" : vehiculo.matricula}) 
    
    return(render(request, "entidades/vehiculoForm.html", {"form" : miForm}))
# -- - --
@login_required
def vehiculoDelete(request, id_vehiculo):
    vehiculoForm = Vehiculo.objects.get(id=id_vehiculo)
    vehiculoForm.delete()
    contexto = {"vehiculos" : Vehiculo.objects.all()}
    return(render(request, "entidades/vehiculos.html", contexto))
# -- - --

# Formulario de búsqueda
@login_required
def buscarVehiculos(request):
    return(render(request, "entidades/buscar.html"))

@login_required
def encontrarVehiculos(request):
    if (request.GET["buscar"]):
        patron = request.GET["buscar"]
        vehiculo = Vehiculo.objects.filter(matricula__icontains=patron) # devuelve lo que encuentra que contenga el patron que se le pasa
        contexto = {"vehiculos" : vehiculo }
    else:
        contexto = {"vehiculos" : Vehiculo.objects.all()}
    return render(request, "entidades/vehiculos.html", contexto)

# *******  FIN VEHICULOS  *******

# *******   PROVEEDORES   *******

@login_required
def proveedoresForm(request):
    if (request.method == "POST"):
        miform = ProveedorForm(request.POST)
        if (miform.is_valid()):
            proveedor_nombre = miform.cleaned_data.get("nombre")
            proveedor_apellido = miform.cleaned_data.get("apellido")
            proveedor_email = miform.cleaned_data.get("email")
            proveedor_direccion = miform.cleaned_data.get("direccion")
            proveedor = Proveedor(nombre = proveedor_nombre, 
                                  apellido = proveedor_apellido, 
                                  email = proveedor_email,
                                  direccion = proveedor_direccion)
            proveedor.save()
            contexto = {"proveedores" : Proveedor.objects.all()}
            return(render(request, "entidades/proveedores.html", contexto))
    else:
        miform = ProveedorForm()
    
    return(render(request, "entidades/proveedorForm.html", {"form" : miform}))
# -- - --
@login_required
def proveedorUpdate(request, id_proveedor):
    proveedor = Proveedor.objects.get(id=id_proveedor)
    if request.method == "POST":
        miForm = ProveedorForm(request.POST)
        if miForm.is_valid():
            proveedor.nombre = miForm.cleaned_data.get("nombre")
            proveedor.apellido = miForm.cleaned_data.get("apellido")
            proveedor.email = miForm.cleaned_data.get("email")
            proveedor.direccion = miForm.cleaned_data.get("direccion")
            proveedor.save()
            contexto = {"proveedores" : Proveedor.objects.all()}
            return(render(request, "entidades/proveedores.html", contexto))
    else:
        miForm = ProveedorForm(initial={"nombre" : proveedor.nombre, 
                                       "apellido" : proveedor.apellido, 
                                       "email" : proveedor.email,
                                       "direccion" : proveedor.direccion}) 
    
    return(render(request, "entidades/proveedorForm.html", {"form" : miForm}))
# -- - --
@login_required
def proveedorDelete(request, id_proveedor):
    proveedorForm = Proveedor.objects.get(id=id_proveedor)
    proveedorForm.delete()
    contexto = {"proveedores" : Proveedor.objects.all()}
    return(render(request, "entidades/proveedores.html", contexto))

# ******* FIN PROVEEDORES *******

# *******    EMPLEADOS    *******

@login_required
def empleadosForm(request):
    if (request.method == "POST"):
        miform = EmpleadoForm(request.POST)
        if (miform.is_valid()):
            empleado_nombre = miform.cleaned_data.get("nombre")
            empleado_apellido = miform.cleaned_data.get("apellido")
            empleado_documento = miform.cleaned_data.get("documento")
            empleado = Empleado(nombre = empleado_nombre, 
                                  apellido = empleado_apellido,
                                  documento = empleado_documento)
            empleado.save()
            contexto = {"empleados" : Empleado.objects.all()}
            return(render(request, "entidades/empleados.html", contexto))
    else:
        miform = EmpleadoForm()
    
    return(render(request, "entidades/empleadoForm.html", {"form" : miform}))
# -- - --
@login_required
def empleadoUpdate(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    if request.method == "POST":
        miForm = EmpleadoForm(request.POST)
        if miForm.is_valid():
            empleado.nombre = miForm.cleaned_data.get("nombre")
            empleado.apellido = miForm.cleaned_data.get("apellido")
            empleado.documento = miForm.cleaned_data.get("documento")
            empleado.save()
            contexto = {"empleados" : Empleado.objects.all()}
            return(render(request, "entidades/empleados.html", contexto))
    else:
        miForm = EmpleadoForm(initial={"nombre" : empleado.nombre, 
                                       "apellido" : empleado.apellido, 
                                       "documento" : empleado.documento}) 
    
    return(render(request, "entidades/empleadoForm.html", {"form" : miForm}))
# -- - --
@login_required
def empleadoDelete(request, id_empleado):
    empleadoForm = Empleado.objects.get(id=id_empleado)
    empleadoForm.delete()
    contexto = {"empleados" : Empleado.objects.all()}
    return(render(request, "entidades/empleados.html", contexto))

# *******  FIN EMPLEADOS  *******


# * * * Login / Logout / Registración

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        
        user = authenticate(request, username=usuario, password=clave)

        if (user is not None):
            login(request, user)

            # Buscar Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            return (render(request, "entidades/index.html"))
        else:
            return (redirect(reverse_lazy("login")))
    else:
        miForm = AuthenticationForm()
    
    return render(request, "entidades/login.html", {"form": miForm} )

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            # usuario = miForm.cleaned_data.get("username")
            miForm.save()
            
            return (redirect(reverse_lazy("home")))
    else:
        miForm = RegistroForm()
    
    return render(request, "entidades/registro.html", {"form": miForm} )

# EDICION DE PERFIL / AVATAR

@login_required
def editProfile(request):
    usuario = request.user
    if (request.method == "POST"):
        miForm = UserEditoForm(request.POST)
        if (miForm.is_valid()):
            user = User.objects.get(username = usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
        
    else:
        miForm = UserEditoForm(instance = usuario)

    return render(request, "entidades/editarPerfil.html", {"form" : miForm})

@login_required
def agregarAvatar(request):
    if (request.method == "POST"):
        miForm = AvatarForm(request.POST, request.FILES)
        if (miForm.is_valid()):
            usuario = User.objects.get(username = request.user)
            imagen = miForm.cleaned_data["imagen"]
            # Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if (len(avatarViejo) > 0):
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            # Guardamos avatar
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            # Enviamos la imágen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen

            return redirect(reverse_lazy("home"))
        
    else:
        miForm = AvatarForm()

    return render(request, "entidades/agregarAvatar.html", {"form" : miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "entidades/cambiarClave.html"
    success_url = reverse_lazy("home")