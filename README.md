# Motor de Base de Datos Relacional basado en Teoría de Conjuntos

## Descripción
Este proyecto implementa un motor de base de datos relacional utilizando conceptos fundamentales de la teoría de conjuntos. La implementación se realiza en Python usando Jupyter Notebook, demostrando la relación entre las operaciones de conjuntos y las funcionalidades típicas de un SGBD relacional.

## Características Principales
- Implementación de operaciones fundamentales de teoría de conjuntos
- Sistema de tipos y validación de datos
- Optimizaciones mediante índices y caché
- Soporte para restricciones de integridad
- Documentación completa y ejemplos prácticos

## Requisitos del Sistema
- Python 3.8 o superior
- Jupyter Notebook
- Google Colab (recomendado para ejecución)
- Paquetes Python especificados en `requirements.txt`

## Instalación
1. Clonar el repositorio:
```bash
git clone [URL_del_repositorio]
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Abrir el notebook en Google Colab o Jupyter:
   - Para Google Colab: Subir el archivo `motor_bd_conjuntos.ipynb`
   - Para Jupyter local: Ejecutar `jupyter notebook` y abrir el archivo

## Estructura del Proyecto
```
├── README.md
├── requirements.txt
├── motor_bd_conjuntos.ipynb
├── presentacion/
│   └── presentacion.pdf
└── docs/
    ├── guia_usuario.md
    └── guia_presentacion.md
```

## Uso Básico
1. Abrir el notebook `motor_bd_conjuntos.ipynb`
2. Ejecutar las celdas en orden
3. Seguir los ejemplos y ejercicios propuestos

## Operaciones Implementadas
1. **Operaciones Básicas**
   - Unión (∪)
   - Intersección (∩)
   - Diferencia (-)
   - Producto Cartesiano (×)

2. **Operaciones Relacionales**
   - Selección (σ)
   - Proyección (π)
   - Join (⋈)

3. **Funcionalidades Avanzadas**
   - Validación de tipos
   - Restricciones de integridad
   - Optimizaciones
   - Sistema de caché

## Ejemplos de Uso
```python
# Crear el motor de base de datos
motor = MotorBD()

# Crear una tabla
estudiantes = motor.crear_tabla("estudiantes", [
    DefinicionColumna("id", TipoDato.INTEGER, {Restriccion.PRIMARY_KEY}),
    DefinicionColumna("nombre", TipoDato.STRING, {Restriccion.NOT_NULL})
])

# Agregar datos
estudiantes.agregar_registro((1, "Ana"))
estudiantes.agregar_registro((2, "Carlos"))

# Realizar consultas
resultado = motor.seleccion(estudiantes, lambda x: x[1].startswith("A"))
```

## Contribución al Proyecto
1. Fork del repositorio
2. Crear rama para nueva funcionalidad
3. Commit y push de cambios
4. Crear Pull Request

## Autores
[Nombres de los integrantes del equipo]

## Licencia
Este proyecto es parte de un trabajo académico para la asignatura de Estructuras Computacionales Discretas. 