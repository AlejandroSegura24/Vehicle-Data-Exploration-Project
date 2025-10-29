# Vehicle-Data-Exploration-Project

Este proyecto es una demostración práctica de habilidades en análisis de datos, utilizando Python y bibliotecas como Pandas, Matplotlib y Seaborn. Se enfoca en la limpieza, exploración y filtrado de un dataset de anuncios de venta de autos, simulando escenarios reales de toma de decisiones para diferentes perfiles de clientes.

## Descripción del Proyecto

El objetivo principal es procesar y analizar un conjunto de datos de vehículos usados (obtenido de Kaggle), aplicando técnicas de limpieza de datos y análisis exploratorio. El proyecto se divide en notebooks independientes, cada uno abordando un enfoque específico para mostrar conocimientos en manipulación de datos, visualización y toma de decisiones basada en evidencia.

A través de este trabajo, se demuestra la capacidad para:
- Limpiar y preparar datos (manejo de nulos, duplicados, conversión de tipos).
- Realizar análisis exploratorio (EDA) con filtrado progresivo y visualizaciones.
- Aplicar lógica de negocio para responder preguntas específicas de "clientes" simulados.
- Optimizar código mediante modularización (uso de un módulo `utils.py` para reutilización).

Este proyecto refleja el aprendizaje adquirido en cursos o prácticas de análisis de datos, priorizando claridad, reproducibilidad y mejores prácticas.

## Fuentes de Datos

- Dataset original: [Used Car Catalog](https://www.kaggle.com/datasets/lepchenkov/usedcarscatalog/data) (descárgalo y colócalo como `cars.csv` en la raíz del proyecto).

## Estructura del Proyecto

- **`.gitignore`**: Archivo para especificar archivos y carpetas que Git debe ignorar (ej. datos temporales, entornos virtuales, archivos de IDE).
- **`environment.yml`**: Archivo de configuración para crear un entorno Conda con todas las dependencias necesarias (Python, bibliotecas como Pandas, Seaborn, etc.).
- **`README.md`**: Este archivo, con descripción del proyecto, instrucciones de instalación y uso.
- **`Data/`**: Carpeta que contiene los datasets utilizados.
  - `cars.csv`: Dataset original (descárgalo de Kaggle y colócalo aquí).
  - `carros_parte1.csv`, `carros_parte2.csv`, `carros_parte3.csv`: Subconjuntos generados durante la limpieza.
- **`Notebooks/`**: Carpeta con los notebooks de análisis.
  - `1_limpieza_dataset.ipynb`: Limpieza inicial del dataset completo. Incluye eliminación de columnas irrelevantes, imputación de valores nulos, manejo de duplicados y separación en subconjuntos por marcas.
  - `2_exploracion_marcas_caracteristicas.ipynb`: Análisis exploratorio enfocado en autos con características de alto valor (transmisión automática, motor híbrido/gasolina, bajo kilometraje). Simula la búsqueda de un coche "barato pero premium".
  - `3_seleccion_marcas_economicas.ipynb`: Exploración de opciones económicas para uso diario en ciudad (bajo consumo de combustible, precio accesible, transmisión automática).
  - `4_exploracion_marcas_costosas.ipynb`: Análisis de vehículos de lujo (marcas como BMW, Mercedes-Benz, Land Rover) con filtros por estado, kilometraje y año de producción.
- **`src/`**: Carpeta con módulos auxiliares.
  - `utils.py`: Módulo auxiliar con funciones reutilizables para configuración de gráficas y rastreo de reducciones de datos.


## Requisitos e Instalación

### Prerrequisitos
- Python 3.8 o superior.
- Bibliotecas: `pandas`, `numpy`, `matplotlib`, `seaborn`. Instálalas con:
  ```
  pip install pandas numpy matplotlib seaborn
  ```

### Cómo ejecutar
1. Clona el repositorio:
   ```
   git clone https://github.com/AlejandroSegura24/Vehicle-Data-Exploration-Project.git
   cd Vehicle-Data-Exploration-Project
   ```
2. Descarga `cars.csv` de Kaggle y colócalo en la raíz del proyecto.
3. Abre los notebooks en Jupyter Notebook o VS Code, y ejecuta las celdas en orden (comienza por `1_limpieza_dataset.ipynb`).
4. Los notebooks generan archivos CSV intermedios automáticamente.

## Tecnologías y Habilidades Demostradas

- **Lenguaje**: Python.
- **Bibliotecas clave**:
  - `Pandas`: Manipulación y filtrado de datos.
  - `Seaborn` y `Matplotlib`: Visualización de datos (gráficos de barras, dispersión, etc.).
  - `NumPy`: Operaciones numéricas básicas.
- **Habilidades**:
  - Limpieza de datos (imputación, eliminación de duplicados).
  - Análisis exploratorio (EDA) con filtrado progresivo y visualizaciones.
  - Filtrado condicional y modularización de código.
  - Interpretación de resultados para decisiones prácticas.
  - Documentación clara en notebooks (mezcla de código y explicaciones en Markdown).

## Resultados e Insights Principales

- **Limpieza**: El dataset se redujo de ~38.000 filas a subconjuntos manejables, eliminando ruido y asegurando calidad.
- **Análisis por perfil**:
  - Para autos premium: Lexus LS destaca por bajo kilometraje y precio competitivo.
  - Para económicos: Toyota Prius y Fiat 500 ofrecen eficiencia en ciudad.
  - Para lujo: Mercedes-Benz proporciona mayor variedad que BMW o Land Rover.
- Los notebooks incluyen visualizaciones que muestran tendencias (ej. relación entre precio y kilometraje), y conclusiones accionables para cada escenario.

## Contribuciones y Mejoras Futuras

Este proyecto es una base sólida para análisis de datos. Posibles mejoras:
- Integrar machine learning para predicción de precios.
- Agregar más visualizaciones interactivas (ej. con Plotly).
- Expandir a datasets más grandes o en tiempo real.

Si encuentras errores o tienes sugerencias, ¡abre un issue o pull request!

## Autor
- **Nombre**: David Alejandro Segura 
- **Contacto**: davidalejandrocmbs@gmail.com
- **Propósito**: Proyecto educativo para demostrar competencias en análisis de datos con Python.
