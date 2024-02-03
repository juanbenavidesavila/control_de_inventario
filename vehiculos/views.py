from django.shortcuts import render
from .forms import VehiculoForm
from .models import Vehiculo


# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)


# Crear una function que se llame v_list
# Que tenga variable context = {}
# Que tenga el return render
# Que llame al archivo list.html

# Dentro de la variable context
# incluir el listado de vehiculos
# Vehiculo.objects.all()
from django.contrib.auth.decorators import login_required, permission_required


@login_required(login_url="/admin/login/")
@permission_required('vehiculos.visualizar_catalogo',
                     login_url="/admin/login/")
def v_list(request):
    datos = Vehiculo.objects.all()
    if request.GET.get('modelo', None) != None: #cuando sea diferente
      datos = datos.filter(modelo__icontains = request.GET.get('modelo'))
      
    if request.GET.get('marca', None) != None: #cuando sea diferente
      datos = datos.filter(marca__icontains = request.GET.get('marca'))
      
    context = {'cars': datos}
    return render(request, "list.html", context)
    # Crear el archivo list.html en templates
    # Crear la url que apunte a v_list
    # vehiculo/list


@login_required(login_url="/admin/login/")
@permission_required('vehiculos.add_vehiculo', login_url="/admin/login/")
def v_add(request):
    if request.method == 'POST':  # Si la peticion proviene de un metodo POST
        data = VehiculoForm(
            request.POST)  # Datos del metodo post inserto en el form
        if data.is_valid():  # Los datos cruzan las validaciones
            data.save()  # Guarda en base de datos

    # Se muestra cuando la peticion no sea POST
    # Se muestra cuando la peticion POST ha terminado
    context = {"form": VehiculoForm()}
    return render(request, "add.html", context)
