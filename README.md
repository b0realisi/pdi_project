# Proyecto Final de Procesamiento Digital de Imágenes

Este proyecto aplica técnicas de mejora y restauración sobre imágenes antiguas. Está desarrollado en Python con un enfoque modular y orientado a objetos.

## Estructura del proyecto

```
PDI_PROJECT/
├── data/
│   ├── input/               # Imágenes originales
│   └── output/              # Imágenes procesadas
│
├── src/
│   ├── core/                # Representación de imágenes
│   ├── io/                  # Lectura y guardado
│   ├── preprocessing/       # Filtros individuales
│   ├── restoration/         # Clases orquestadoras
│   ├── cli.py               # Interfaz CLI
│   └── main.py              # Punto de entrada
│
├── scripts/
│   ├── batch_process.py     # Procesamiento por lotes
│   └── show_histogram.py    # Comparación de histogramas
│
├── tests/
│   └── test_basic_pipeline.py # Prueba automática con pytest
│
├── Dockerfile
├── docker-compose.yml
├── README.md
├── requirements.txt
└── informe_tecnico.md
```

---


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

4. Usos

### Modo automático (seleccioná qué filtros aplicar):

Si no se indican filtros, se aplican:

- Ajuste de brillo (factor=1.05)
- Ecualización de histograma
- Filtro Gaussiano (kernel=5)

```bash
python src/main.py --input data/input/imagen1.jpg --output data/output/imagen1_restaurada.jpg
```

### Modo personalizado (selección de filtros a aplicar):

```bash
python -m src.main --input data/input/foto1.jpg --output data/output/foto1_custom.jpg --brightness --equalize --contrast --clahe
```
#### Filtros disponibles:

- `--brightness` + `--brightness-factor` → Ajuste de brillo

- `--contrast` + `--contrast-alpha` → Ajuste de contraste

- `--equalize` → Ecualización de histograma global

- `--clahe` + `--clahe-clipLimit` + `--clahe-tileGridSize` → Ecualización adaptativa

- `--gaussian` + `--gaussian-kernel` → Suavizado Gaussiano

- `--median` + `--median-kernel` → Filtro de mediana (ruido)

- `--bilateral` + `--bilateral-sigmaColor` + `--bilateral-sigmaSpace` → Suavizado con preservación de bordes

- `--sharpen` → Filtro de nitidez

- `--sobel` → Realce de bordes con operador Sobel

- `-grayscale` → Conversión a escala de grises

- `--colorize` + `--color-map` → Colorización artificial estilo térmico

- `--inpaint` + `--inpaint-radius` → Reconstrucción simple con máscara fija


### Scripts adicionales

Muestra el histograma antes y después de aplicar ecualización:

```bash
python scripts/show_histogram.py
```

Aplica el pipeline automático a todas las imágenes en data/input/ y guarda en data/output/:

```bash
python scripts/batch_process.py

```

## Docker (opcional)

### ¿Para qué sirve?
Permite correr el proyecto sin instalar dependencias localmente. Empaqueta todo en un contenedor.

### Construir imagen manualmente:
```bash
docker build -t pdi_app .
```

### Ejecutar contenedor:
```bash
docker run --rm -v $(pwd)/data:/app/data pdi_app --input data/input/foto1.jpg --output data/output/foto1_out.jpg --brightness --equalize
```

### Usar docker-compose (más fácil):
```bash
docker-compose up
```

- Se puede editar el archivo `docker-compose.yml` para cambiar filtros y nombres de archivos.

---

## Automatización de pruebas

El proyecto incluye un test automático con `pytest`:

```bash
pytest
```

Ubicación del test:
```
tests/test_basic_pipeline.py
```

### ¿Qué verifica?
- Que el filtro de brillo se aplique correctamente.
- Que la imagen resultante exista y tenga las mismas dimensiones que la original.

---

## Créditos

Desarrollado como proyecto final para la materia **Procesamiento de Imágenes Digitales**
