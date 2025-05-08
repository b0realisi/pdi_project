# Proyecto Final de Procesamiento Digital de Imágenes

Este proyecto aplica técnicas de mejora y restauración sobre imágenes antiguas. Está desarrollado en Python con un enfoque modular y orientado a objetos.

## Estructura del proyecto

PDI_PROJECT/
│
├── data/
│ ├── input/ # Imágenes originales
│ └── output/ # Imágenes procesadas
│
├── src/
│ ├── core/ # Representación de imágenes
│ ├── io/ # Lectura y guardado
│ ├── preprocessing/ # Filtros individuales
│ ├── restoration/ # Clases orquestadoras (ImageRestorer, ImageEnhancer)
│ ├── cli.py # Línea de comandos
│ └── main.py # Punto de entrada


## Instalación

1. Clona el repositorio o copia el proyecto.
2. Crea un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows
```

3. Instalar las dependencias necesarias
```bash
pip install -r requirements.txt
```

4. Uso

```bash
python src/main.py --input data/input/imagen1.jpg --output data/output/imagen1_restaurada.jpg
```

### Modo personalizado (seleccioná qué filtros aplicar):

```bash
python -m src.main --input data/input/foto1.jpg --output data/output/foto1_custom.jpg --brightness --equalize --sobel
```
#### Filtros disponibles:
--brightness` → Ajusta el brillo (factor fijo 1.2)
--equalize` → Ecualización de histograma (mejora el contraste)
--gaussian` → Suavizado con filtro Gaussiano (kernel 5)
--sobel` → Realce de bordes con operador de Sobel

## Créditos

Desarrollado como proyecto final para la materia **Procesamiento de Imágenes Digitales**
