# Proyecto Final de Procesamiento Digital de Imágenes

Este proyecto aplica técnicas de mejora y restauración sobre imágenes antiguas. No se utiliza Machine Learning. Está desarrollado en Python con un enfoque modular y orientado a objetos.

## Estructura del proyecto

PDI_PROJECT/
│
├── data/
│ ├── input/ # Imágenes originales
│ └── output/ # Imágenes restauradas
│
├── src/
│ ├── core/ # Clase base Image
│ ├── io/ # Lector y escritor de imágenes
│ ├── preprocessing/ # Filtros de mejora (brillo, suavizado, etc.)
│ ├── restoration/ # Restaurador que orquesta los filtros
│ ├── cli.py # Argumentos desde la línea de comandos
│ └── main.py # Punto de entrada
│
├── README.md
├── requirements.txt
└── informe_tecnico.pdf


## Instalación

1. Clona el repositorio o copia el proyecto.
2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows
```

3. Instala las dependencias necesarias
```bash
pip install -r requirements.txt
```

4. Uso

```bash
python src/main.py --input data/input/imagen1.jpg --output data/output/imagen1_restaurada.jpg
```