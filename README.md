
# Sistema de Gestión de Recursos Humanos

Este proyecto es un sistema de gestión de recursos humanos que permite administrar empleados, departamentos y puestos de trabajo.

# Backend

Esta sección describe el backend del proyecto.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación](#instalación)
- [Uso](#uso)
- [Endpoints de la API](#endpoints-de-la-api)


## Características
- Gestión de empleados, incluyendo la creación, actualización y eliminación.
- Gestión de departamentos y puestos de trabajo.
- API RESTful para la interacción con el sistema.

## Tecnologías Utilizadas

- **Python**: Versión 3.8 o superior.
- **Flask**: Framework utilizado para el desarrollo del backend.
- **Flask-Restx**: Para construir la API RESTful.
- **SQLAlchemy**: ORM utilizado para la base de datos.
- **PostgreSQL**: Sistema de gestión de bases de datos.
- **DBeaver**: Herramienta para la gestión de la base de datos.

### Instalación

1. Clona el repositorio:
    ```bash
    git clone <URL del repositorio>
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd <nombre del directorio>
    ```
3. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```
4. Activa el entorno virtual:
    - En Windows:
      ```bash
      venv\Scripts\activate
      ```

5. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
6. Configura la base de datos y ejecuta las migraciones:
    ```bash
    flask db upgrade
    ```
7. Ejecuta la aplicación:
    ```bash
    flask run

    o

    python app.py
    ```
   
### Conexión a la Base de Datos
Para establecer la conexión con la base de datos PostgreSQL, asegúrate de tener PostgreSQL instalado y en funcionamiento. Luego, configura la cadena de conexión en el archivo de configuración de la aplicación. 

Cómo se puede configurar la conexión en tu archivo de configuración (`app.py`):

```python
SQLALCHEMY_DATABASE_URI = 'postgresql://usuario:contraseña@localhost/nombre_base_datos'
SQLALCHEMY_TRACK_MODIFICATIONS = False

     
   ```

## Uso

1. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

2. Accede a la API en `http://localhost:5000`.

## Endpoints de la API

### Departamentos
- **GET** `/departamento` - Obtiene todos los departamentos.
- **POST** `/departamento` - Crea un nuevo departamento.
- **GET** `/departamento/<int:id>` - Obtiene un departamento específico por ID.
- **PUT** `/departamento/<int:id>` - Actualiza un departamento existente.
- **DELETE** `/departamento/<int:id>` - Elimina un departamento.

### Empleados
- **GET** `/empleado` - Obtiene todos los empleados.
- **POST** `/empleado` - Crea un nuevo empleado.
- **GET** `/empleado/<int:id>` - Obtiene un empleado específico por ID.
- **PUT** `/empleado/<int:id>` - Actualiza un empleado existente.
- **DELETE** `/empleado/<int:id>` - Elimina un empleado.

### Puestos
- **GET** `/puesto` - Obtiene todos los puestos.
- **POST** `/puesto` - Crea un nuevo puesto.
- **GET** `/puesto/<int:id>` - Obtiene un puesto específico por ID.
- **PUT** `/puesto/<int:id>` - Actualiza un puesto existente.
- **DELETE** `/puesto/<int:id>` - Elimina un puesto.

____________________________________

# Frontend  Coming Soon
Esta sección describe el frontend del proyecto.

### Descripción - - Coming Soon

Descripción del frontend, incluyendo la tecnología utilizada y la estructura.

### Requisitos - - Coming Soon

Lista de requisitos para el frontend, si es diferente a los del backend.

### Instalación - - Coming Soon

Pasos para instalar y ejecutar el frontend.

### Funcionalidades - - Coming Soon

Lista de funcionalidades que ofrece el frontend.
