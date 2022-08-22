# from django.shortcuts import HttpResponse
from django.shortcuts import render


# Pantalla Inicial

def inicio(request):
    data = {
        'titulo': "Inicio"
    }
    return render(request, 'base.html', data)


def medico(request):
    data = {
        'titulo': 'Gestión Médica',
    }
    return render(request, 'medico/medico.html', data)


def listempleado(request):
    data = {
        'titulo': 'LISTA DE EMPLEADOS',
        'listar_url': '/listempleado',
    }

    return render(request, "medico/empleados/listempleado.html", data)


def listmedicamento(request):
    data = {
        'titulo': 'LISTA DE MEDICAMENTOS',
        'crear_url': '/formmedicamento',
        'listar_url': '/listmedicamento',
        'text_Register': 'Registrar medicamento',
    }
    return render(request, "medico/medicamento/listmedicamento.html", data)


def formmedicamento(request):
    data = {
        'titulo': 'FORMULARIO DE MEDICAMENTOS',
        'crear_url': '/listmedicamento',
        'listar_url': '/listmedicamento',
        'text_Guardar': 'Guardar Registro',
    }
    return render(request, "medico/medicamento/formmedicamento.html", data)


def listreceta(request):
    data = {
        'titulo': 'RECETAS MÉDICAS',
        'crear_url': '/formreceta',
        'vista_url': '/vistareceta',
        'listar_url': '/listreceta',
        'text_Register': 'Crear nueva Receta',
    }

    return render(request, "medico/receta/listreceta.html", data)

def filtroUrl(request):
    data = '/ejem'

    return render(request, "ejem.html", {'filtro_url': data})


def vistareceta(request):
    data = {
        'titulo': 'VISTA DE LA RECETA MÉDICA',
        'crear_url': '/listreceta',
        'listar_url': '/listreceta',
        'text_Guardar': 'Aceptar',
    }

    return render(request, "medico/receta/vistareceta.html", data)


def formreceta(request):
    data = {
        'titulo': 'GENERAR NUEVA RECETA',
        'crear_url': '/listreceta',
        'listar_url': '/listreceta',
        'text_Guardar': 'Guardar receta',
    }

    return render(request, "medico/receta/formreceta.html", data)


def listdiagnostico(request):
    data = {
        'titulo': 'LISTA DE DIAGNÓSTICOS',
        'crear_url': '/formdiagnostico',
        'listar_url': '/listdiagnostico',
        'text_Register': 'Nuevo Registro',
    }

    return render(request, "medico/diagnostico/listdiagnostico.html", data)


def formdiagnostico(request):
    data = {
        'titulo': 'FORMULARIO DE DIAGNÓSTICOS',
        'crear_url': '/listdiagnostico',
        'listar_url': '/listdiagnostico',
        'text_Guardar': 'Guardar registro',
    }

    return render(request, "medico/diagnostico/formdiagnostico.html", data)


def listhistorclin(request):
    data = {
        'titulo': 'LISTA DE INFORMES CLÍNICOS',
        'crear_url': '/formhistorclin',
        'vista_url': '/editformHC',
        'listar_url': '/listhistorclin',
        'text_Register': 'Crear Informe',
    }

    return render(request, "medico/historialClinico/listhistorclin.html", data)


def formhistorclin(request):
    data = {
        'titulo': 'HISTORIAL CLÍNICO',
        'crear_url': '/listhistorclin',
        'listar_url': '/listhistorclin',
        'text_Guardar': 'Guardar registro',
    }

    return render(request, "medico/historialClinico/formhistorclin.html", data)


def editformHC(request):
    data = {
        'titulo': 'HISTORIAL CLINICO',
        'crear_url': '/listhistorclin',
        'listar_url': '/listhistorclin',
        'generar_receta': '/formreceta',
        'text_Guardar': 'Guardar',
    }

    return render(request, "medico/historialClinico/editformHC.html", data)