# Todo CLI - Gestor de Tareas en Python

Una aplicación de línea de comandos (CLI) sencilla para gestionar tareas pendientes, construida con Python.

# Estructura del Proyecto

todo-cli/
├── todo_app/          # Paquete con la lógica de la aplicación
│   ├── __init__.py    # Archivo de inicialización del paquete
│   ├── storage.py     # Manejo de persistencia JSON
│   └── todo.py        # Modelos de datos y lógica de negocio
├── tests/             # Directorio de pruebas unitarias
│   ├── __init__.py
│   └── test_todo.py   # Archivos de prueba para pytest
├── cli.py             # Punto de entrada de la aplicación (CLI)
├── requirements.txt   # Lista de dependencias del proyecto
├── .gitignore         # Archivos y carpetas ignorados por Git
└── README.md          # Documentación del proyecto

# Configurar el entorno virtual
* python -m venv .venv
# Activar en Windows:
* .\.venv\Scripts\activate

# Características
* Agregar tareas con descripción.
* Listar todas las tareas pendientes.
* Marcar tareas como completadas.
* Eliminar tareas.
* Persistencia de datos en formato JSON.

# Uso
* Añadir tarea: python cli.py add "Estudiar Python"
* Listar tareas: python cli.py list
* Completar tarea: python cli.py done <ID>
* Borrar tarea: python cli.py delete <ID>
* Testear funciones: python -m pytest 

