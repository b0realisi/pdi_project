# Proyecto Final de Procesamiento Digital de Imágenes

Este proyecto aplica técnicas de mejora y restauración sobre imágenes antiguas. Está desarrollado en Python con un enfoque modular y orientado a objetos.

## Estructura del proyecto

```nPDI_PROJECT/`n│`n├── data/`n│   ├── input/         # Imágenes originales`n│   └── output/        # Imágenes procesadas`n│`n├── src/`n│   ├── core/                  # Clase base Image`n│   ├── io/                    # Lector y escritor de imágenes`n│   ├── preprocessing/         # Filtros individuales`n│   ├── restoration/           # Clases orquestadoras (ImageRestorer, ImageEnhancer)`n│   ├── cli.py                 # CLI basada en argparse`n│   └── main.py                # Punto de entrada principal`n│`n├── README.md`n├── requirements.txt`n└── informe_tecnico.md`n````n`


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
- `--brightness` → Ajusta el brillo (factor fijo 1.2)
- `--equalize` → Ecualización de histograma (mejora el contraste)
- `--gaussian` → Suavizado con filtro Gaussiano (kernel 5)
- `--sobel` → Realce de bordes con operador de Sobel

## Créditos

Desarrollado como proyecto final para la materia **Procesamiento de Imágenes Digitales**