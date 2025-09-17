# Liser - Plataforma de Listas de Productos

**Liser** es una aplicación web que permite a creadores de contenido organizar y compartir listas de productos de manera visual y organizada.

## ¿Qué es Liser?

Es una plataforma enfocada en listas de productos donde los creadores pueden mostrar:
- Lo que llevan en su maleta de viaje
- Su setup de trabajo 
- Sus productos favoritos de cualquier sector
- Elementos de su hogar
- Cualquier colección de productos que quieran compartir

## Características Principales

### Para Creadores
- **Organización intuitiva**: Crea listas principales y sublistas para categorizar productos
- **Información completa**: Cada producto puede tener imagen, descripción, enlaces, videos, códigos de descuento
- **Control de visibilidad**: Listas privadas, públicas abiertas o solo para usuarios registrados
- **Gestión de tags**: Organiza y categoriza tus listas con etiquetas personalizadas

### Para Seguidores
- **Visualización clara**: Interfaz limpia para explorar listas de productos
- **Favoritos**: Guarda listas y productos de interés
- **Acceso directo**: Enlaces directos a productos, videos e Instagram
- **Códigos de descuento**: Copia códigos promocionales con un click
- **Listas propias**: Crea tus propias listas inspirándote en otros creadores

## Tecnologías

- **Backend**: Django 5.2.6
- **Base de datos**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Autenticación**: Sistema de usuarios personalizado con roles

## Estructura del Proyecto

### Modelos Principales
- **CustomUser**: Usuarios con roles (usuario/admin)
- **BagList**: Lista principal de productos
- **tBagList**: Sublistas dentro de una BagList
- **Item**: Productos del catálogo
- **Tag**: Etiquetas para organizar listas
- **Favorite**: Sistema de favoritos

### Funcionalidades por Implementar
- [ ] Dashboard de usuario
- [ ] CRUD completo de BagLists
- [ ] Gestión de Items
- [ ] Sistema de búsqueda y filtros
- [ ] Panel de administración
- [ ] API REST para integración con apps móviles

## Instalación y Desarrollo

### Prerequisitos
- Python 3.8+
- MySQL
- Django 5.2.6

### Configuración Local
1. Clona el repositorio:
```bash
git clone https://github.com/excusasclub/liser-django.git
cd liser-django
```

2. Instala las dependencias:
```bash
pip install django mysqlclient
```

3. Configura tu base de datos en `settings.py`

4. Ejecuta las migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crea un superusuario:
```bash
python manage.py createsuperuser
```

6. Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

## Roadmap

### Fase 1 - MVP
- [x] Modelos de datos
- [x] Vista básica de BagList
- [ ] Dashboard principal
- [ ] CRUD de BagLists e Items
- [ ] Sistema de autenticación

### Fase 2 - Funcionalidades Avanzadas
- [ ] Sistema de búsqueda
- [ ] Filtros por tags
- [ ] Perfil público de usuarios
- [ ] Sistema de seguidores

## Contribuir

Este proyecto está en desarrollo activo. Las contribuciones son bienvenidas.

## Licencia

Este proyecto está bajo desarrollo privado.

---