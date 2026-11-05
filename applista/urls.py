from django.urls import path, include
from . import views
from rest_framework import routers
from applista import views



urlpatterns = [
    path('', views.lista_tareas, name='base'),  # Redirige a la lista directamente
    path('lista/', views.lista_tareas, name='lista_tareas'),
    path('agregar/', views.agregar_tarea, name='agregar_tarea'),
    path('eliminar/<int:id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('modificar/<int:id>/', views.modificar_tarea, name='modificar_tarea'),
    path('api/puro/tareas/<int:id>/', views.api_tarea_por_id_puro, name='api_tarea_puro'),
    path('api/drf/tareas/<int:id>/', views.api_tarea_por_id_drf, name='api_tarea_drf'),
    # path('api/drf/tareas/', views.api_tareas_drf, name='api_tareas_drf'),
    path( 'api_auth/', include ('rest_framework.urls')),
]