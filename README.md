# Gestor de tareas

Aplicación web sencilla para crear, listar, modificar y eliminar tareas. También incluye dos endpoints de consulta de tareas en formato JSON: uno implementado directamente con Django y otro con Django REST Framework.

## Tecnologías

- Python 
- Django 5.2
- Django REST Framework
- SQLite

## Requisitos

- Python 3.11 (versión usada en el entorno del proyecto)
- `pip`

## Instalación y ejecución en Windows

Ejecutá estos pasos desde PowerShell, ubicándote en la carpeta del proyecto (donde está `manage.py`).

### 1. Crear un entorno virtual

```powershell
py -m venv .venv
```

### 2. Activar el entorno virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación por la política de ejecución, podés habilitarla solo para la sesión actual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```powershell
python -m pip install --upgrade pip
python -m pip install "Django>=5.2,<6.0" djangorestframework requests
```

`requests` se utiliza en el cliente de ejemplo `cliente_json.py`.

### 4. Crear las tablas de la base de datos

```powershell
python manage.py migrate
```

La aplicación usa SQLite y guarda la base de datos en `db.sqlite3`.

### 5. Iniciar el servidor

```powershell
python manage.py runserver
```

Abrí [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador. Para detener el servidor, presioná `Ctrl+C` en PowerShell.

## Uso

- **Listar tareas:** la página principal muestra las tareas y su estado.
- **Agregar:** elegí “Agregar Tarea” y completá el formulario.
- **Modificar:** usá “Editar” en la tarea que quieras cambiar.
- **Eliminar:** usá “Eliminar” y confirmá la acción.
- **Administración:** entrá a [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). Para crear un usuario administrador, ejecutá `python manage.py createsuperuser` y seguí las instrucciones.

## API

Los endpoints reciben el identificador de una tarea en la URL:

| Método | Ruta | Acceso | Descripción |
|---|---|---|---|
| `GET` | `/api/puro/tareas/<id>/` | Sin autenticación | Devuelve la tarea como JSON, construido directamente con Django. |
| `GET` | `/api/drf/tareas/<id>/` | Requiere autenticación | Devuelve la tarea como JSON usando Django REST Framework. |

Ejemplo desde PowerShell para consultar la versión sin autenticación:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/api/puro/tareas/1/
```

Reemplazá `1` por el ID de una tarea existente. Si no existe, el servidor responde con `404`.

La ruta `/api_auth/` expone las vistas de autenticación de sesión de Django REST Framework. El endpoint de DRF requiere un usuario autenticado; podés iniciar sesión con un usuario creado para el proyecto.

## Estructura principal

```text
.
├── applista/
│   ├── migrations/       # Migraciones de la base de datos
│   ├── templates/        # Plantillas HTML
│   ├── forms.py          # Formulario de tareas
│   ├── models.py         # Modelo Tarea
│   ├── serializers.py    # Serializador de la API DRF
│   ├── urls.py           # Rutas de la aplicación
│   └── views.py          # Vistas web y endpoints API
├── gestion_tareas/
│   ├── settings.py       # Configuración de Django
│   └── urls.py           # Rutas principales del proyecto
├── cliente_json.py       # Cliente de ejemplo para la API JSON
├── manage.py
└── db.sqlite3            # Base SQLite (se crea al migrar)
```

## Modelo de tarea

Cada tarea contiene un título, una descripción opcional, un indicador de si está completada y la fecha de su última modificación.

## Ejecutar las pruebas

```powershell
python manage.py test
```

El proyecto todavía no incluye pruebas funcionales automatizadas.

## Nota de seguridad

La configuración actual está preparada para desarrollo local. Antes de publicar la aplicación, revisá la configuración de Django para producción (por ejemplo, `DEBUG`, `ALLOWED_HOSTS` y la clave secreta).
