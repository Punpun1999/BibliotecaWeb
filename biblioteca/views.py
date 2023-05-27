from django.shortcuts import render, get_object_or_404, redirect
from biblioteca.models import Empleado, Autor

# Create your views here.
def desactivar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    
    if empleado.activo:
        empleado.activo = False
        empleado.save()
        mensaje = "Empleado desactivado correctamente"
    else:
        mensaje = "Empleado ya esta desactivado"
    
    return render(request, 'desactivar_empleado.html',{'mensaje':mensaje})

def activar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)

    if not empleado.activo:
        empleado.activo = True
        empleado.save()
        mensaje = "Empleado activado correctamente."
    else:
        mensaje = "Empleado ya está activo."

    return render(request, 'mensaje_activacion.html', {'mensaje': mensaje})

def registrar_empleado(request):
    if request.POST:
        nombre_empleado = request.POST["nombre"]
        apellido_empleado = request.POST["apellido"]
        numeroLeg_empleado = request.POST["numero_legajo"]

        Empleado.objects.create(
        nombre = nombre_empleado,
        apellido = apellido_empleado,
        numero_legajo = numeroLeg_empleado
        )
    return render(request,"biblioteca/nuevos_empleados.html")

def listado_empleados(request):
    lista_empleados = Empleado.objects.all()

    return render(request, "biblioteca/listado_empleados.html", {"lista_empleados" : lista_empleados})

def actualizar_datos_empleado(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)

    if request.POST:
        nombre_empleado = request.POST["nombre"]
        apellido_empleado = request.POST["apellido"]
        numeroLeg_empleado = request.POST["numero_legajo"]

        empleado.nombre = nombre_empleado
        empleado.apellido = apellido_empleado
        empleado.numero_legajo = numeroLeg_empleado

        empleado.save()

    return render(request, "biblioteca/actualizar_empleado.html", {"empleado" : empleado})

def desactivar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    autor.activo=False
    autor.save()
    return redirect("listado_autores")   

def nuevo_autores(request):
    if request.POST:
        nombre_autor = request.POST["nombre"]
        apellido_autor = request.POST["apellido"]
        nacionalidad_autor = request.POST["nacionalidad"]

        Autor.objects.create(
        nombre = nombre_autor,
        apellido = apellido_autor,
        nacionalidad = nacionalidad_autor
        )
        return redirect("listado_autores")
    return render(request,"biblioteca/nuevos_autores.html")

def actualizar_autores(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)

    if request.method == 'POST':

        nombre_autor = request.POST.get('nombre')
        apellido_autor = request.POST.get('apellido')
        nacionalidad_autor = request.POST.get('nacionalidad')

        autor.nombre = nombre_autor
        autor.apellido = apellido_autor
        autor.nacionalidad = nacionalidad_autor
        autor.save()
        return redirect("listado_autores")

    context = {'autor': autor}
    return render(request, 'biblioteca/actualizar_autor.html', context)

def activar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    autor.activo = True
    autor.save()
    return redirect("listado_autores")

def listado_autores(request):
    lista_autores = Autor.objects.all()

    return render(request, "biblioteca/listado_autores.html", {"lista_autores" : lista_autores})
