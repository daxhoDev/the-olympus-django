# The Olympus - Sistema de Gestión de Gimnasio

Proyecto de gimnasio desarrollado en Django para la universidad.

## Descripción

The Olympus es un sistema web para la gestión de un gimnasio, desarrollado con Django (Python). Incluye funcionalidades básicas para administrar el gimnasio y proporcionar información a los usuarios.

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/daxhoDev/the-olympus-django.git
cd the-olympus-django
```

2. Crear y activar un entorno virtual (recomendado):
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar las migraciones de la base de datos:
```bash
python manage.py migrate
```

5. Crear un superusuario para acceder al panel de administración:
```bash
python manage.py createsuperuser
```

6. Iniciar el servidor de desarrollo:
```bash
python manage.py runserver
```

7. Abrir el navegador en: http://localhost:8000/

## Estructura del Proyecto

```
the-olympus-django/
├── gym/                    # Aplicación principal del gimnasio
│   ├── migrations/        # Migraciones de la base de datos
│   ├── admin.py          # Configuración del panel de administración
│   ├── models.py         # Modelos de datos
│   ├── views.py          # Vistas de la aplicación
│   └── urls.py           # URLs de la aplicación
├── olympus/               # Configuración del proyecto Django
│   ├── settings.py       # Configuración principal
│   ├── urls.py          # URLs principales
│   └── wsgi.py          # Configuración WSGI
├── static/                # Archivos estáticos (CSS, JS, imágenes)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/             # Plantillas HTML
│   ├── base.html         # Plantilla base
│   └── home.html         # Página principal
├── media/                 # Archivos subidos por usuarios
├── manage.py             # Script de gestión de Django
└── requirements.txt      # Dependencias del proyecto
```

## Uso

### Panel de Administración

Accede al panel de administración en: http://localhost:8000/admin/

Usa las credenciales del superusuario que creaste.

### Desarrollo

Para modificar el proyecto:

1. Los modelos se definen en `gym/models.py`
2. Las vistas se definen en `gym/views.py`
3. Las plantillas se encuentran en `templates/`
4. Los archivos estáticos en `static/`

## Comandos Útiles

```bash
# Crear migraciones después de cambios en modelos
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Recolectar archivos estáticos (para producción)
python manage.py collectstatic

# Ejecutar tests
python manage.py test
```

## Tecnologías Utilizadas

- Django 5.2.8 - Framework web de Python
- SQLite - Base de datos (por defecto)
- HTML/CSS - Frontend
- Python Decouple - Gestión de configuración
- Pillow - Procesamiento de imágenes

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto es para uso educativo.

## Contacto

Proyecto desarrollado para la universidad.
