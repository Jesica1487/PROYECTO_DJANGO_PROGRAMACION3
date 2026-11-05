import requests

def consultar_tarea(id_tarea):
    # URL donde está respondiendo nuestro servidor de Django
    url = f'http://127.0.0.1:8000/api/puro/tareas/{id_tarea}/'
    
    print(f"CLIENTE PYTHON: Consultando la API de Tareas (ID: {id_tarea})...")
    
    try:
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            # Traduce el JSON a un diccionario de Python
            tarea = respuesta.json() 
            print("Status 200 OK - Datos Recibidos:")
            print(f"  - ID: {tarea['id']}")
            print(f"  - Título: {tarea['titulo']}")
            print(f"  - Descripción: {tarea['descripcion']}")
            print(f"  - Completada: {tarea['completada']}")
            
        elif respuesta.status_code == 404:
            print(f"Error 404: La tarea con ID {id_tarea} no existe en la BD.")
            
        else:
            print(f"Error en el servidor. Código HTTP: {respuesta.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Error de conexión: ¿Iniciaste el servidor con python manage.py runserver?")

# Llamada de prueba para consultar una tarea (asegurate de usar un ID que exista)
consultar_tarea(id_tarea=3)