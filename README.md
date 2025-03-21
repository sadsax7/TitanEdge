# Titan_Corp

# 🧠 Titan_Corp: Plataforma de Comercio para Estudiantes Universitarios

**Titan_Corp** es una aplicación web construida con **Django 4** y **SQLite3**, diseñada como espacio de comercio exclusivo para estudiantes universitarios. Los usuarios pueden comprar, vender, subastar productos y conectarse dentro de la comunidad universitaria.

Este proyecto es desarrollado en el curso *Tópicos Especiales en Ingenieria de Software* de la *Universidad EAFIT* bajo la arquitectura **MVT (Model-View-Template)**.

---

## 🔧 ¿Cómo ejecutar este proyecto?

### Prerrequisitos

- Python 3.10 o superior
- pip (Python package manager)
- Git
- Entorno virtual (recomendado)

### Instrucciones

```bash
# 1. Clona el repositorio
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

# 2. Crea un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Corre las migraciones
python manage.py migrate

# 5. Ejecuta el servidor
python manage.py runserver
```

### Ruta principal

Accede a la aplicación desde tu navegador en:  
📍 http://localhost:8000/

---

## 🛠 Estructura del Proyecto

Este proyecto sigue el patrón de arquitectura **MVT** de Django:

```
└── manage.py
└── proyecto/                 # Configuración general del proyecto
    └── settings.py
    └── urls.py
└── apps/                     # Aplicaciones internas (modularizadas)
    └── usuarios/
    └── productos/
    └── subastas/
└── templates/                # Templates HTML
└── static/                   # Archivos estáticos (CSS, JS, imágenes)
└── db.sqlite3                # Base de datos SQLite
```

---

## 🔐 Secciones del Sistema

- **Usuario Final:**  
  - Ver productos y subastas
  - Comprar, dejar reseñas, seguir vendedores
  - Acceso restringido solo a lectura e interacción

- **Administrador:**  
  - Gestionar productos, subastas y usuarios
  - Crear/editar/eliminar registros
  - Panel administrativo personalizado

- **Login:**  
  - Autenticación y autorización completa usando `django.contrib.auth`

---

## 💡 Funcionalidades Especiales

1. Búsqueda avanzada de productos
2. Visualización de los 3 productos más vendidos
3. Generación de factura en PDF
4. Visualización de los 4 productos más comentados

---

## 👥 Equipo de Desarrollo

| Nombre                | Rol                                         |
|-----------------------|---------------------------------------------|
| Alejandro Arango      | Full-Stack Developer, Scrum Master          |
| Juan José Villa       | Tester, Backend Developer                   |

---

## 📚 Wiki del Proyecto

Puedes encontrar documentación adicional en la pestaña [Wiki](https://github.com/tu_usuario/tu_repositorio/wiki), que incluye:

- Entregable #1: Logo, Modelo Verbal, Diagramas
- Guía de estilo de programación
- Reglas de programación por capas
- Funcionalidades especiales
- Pantallazos de la app

---

## 📩 Contacto

📩 [aarangom1@eafit.edu.co](mailto:aarangom1@eafit.edu.co) o [jjvillas@eafit.edu.co](mailto:jjvillas@eafit.edu.co])

