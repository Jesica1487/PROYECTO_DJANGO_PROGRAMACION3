from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse  
from .models import Tarea
from .forms import TareaForm
from django.views.decorators.http import require_POST
from .serializers import TareaSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



# Vistas anteriores (base, lista_tareas, agregar_tarea, eliminar_tarea)
def base(request):
    return render(request, 'base.html')

def lista_tareas(request):
    todas_las_tareas = Tarea.objects.all()
    return render(request, 'lista.html', {'mis_tareas': todas_las_tareas})

def agregar_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Tarea agregada correctamente!")
            return redirect("lista_tareas")
    else:
        form = TareaForm()
    return render(request, "agregar.html", {"form": form})

@require_POST
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()
    messages.success(request, "Tarea eliminada correctamente.")
    return redirect('lista_tareas')

def modificar_tarea(request, id):
    
    tarea = get_object_or_404(Tarea, id=id)


    if request.method == "POST":
        # 2. Pasamos request.POST y la instancia existente para sobrescribir
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Tarea modificada correctamente!")
            return redirect("lista_tareas")
    else:
        # 3. Solicitud GET: cargamos el formulario precargado con los datos actuales
        form = TareaForm(instance=tarea)

    return render(request, "modificar.html", {"form": form, "tarea": tarea})
# ==========================================
# VISTAS DE API (TP6 - JSON Puro)
# ==========================================

def api_tarea_por_id_puro(request, id):
    """
    Opción JSON Puro: Busca una tarea por su ID y construye
    la respuesta JSON manualmente sin usar serializers.
    """
    if request.method == 'GET':
        # 1. Buscamos la tarea o devolvemos error 404 si no existe
        tarea = get_object_or_404(Tarea, id=id)
        
        # 2. Armamos un diccionario manualmente con sus datos
        datos = {
            'id': tarea.id,
            'titulo': tarea.titulo,
            'descripcion': tarea.descripcion,
            'completada': tarea.completada
        }
        
        # 3. Retornamos la respuesta JSON
        return JsonResponse(datos)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])

def api_tarea_por_id_drf(request, id):
    """
    Opción Django REST Framework: Busca una tarea por ID
    y la transforma a JSON utilizando TareaSerializer.
    """
    tarea = get_object_or_404(Tarea, id=id)
    
    serializer = TareaSerializer(tarea)
    
    return Response(serializer.data)    