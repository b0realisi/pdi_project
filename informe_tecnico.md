# Informe Técnico - Proyecto Final de Procesamiento Digital de Imágenes

## Integrantes
- [Nombre Apellido]
- [Nombre Apellido]
- [Nombre Apellido]
- [Nombre Apellido]

## Carrera: Tecnicatura en Ciencia de Datos e Inteligencia Artificial  
## Materia: Procesamiento Digital de Imágenes  
## Cuatrimestre: 1C - 2025

---

## 1. Introducción

El presente proyecto tiene como objetivo aplicar técnicas de procesamiento digital de imágenes (PDI) para mejorar la calidad visual de fotografías antiguas. Estas imágenes, debido a su antigüedad y condiciones de almacenamiento, suelen presentar problemas como bajo contraste, desenfoque o ruido. La restauración de imágenes no solo tiene valor histórico y cultural, sino que también es una excelente aplicación de los conceptos fundamentales vistos durante la cursada.

---

## 2. Objetivo

Restaurar imágenes antiguas mediante un conjunto de filtros y transformaciones aplicadas en una arquitectura modular orientada a objetos, sin utilizar técnicas de aprendizaje automático.

---

## 3. Dataset

Se utilizó un conjunto de 29 imágenes antiguas descargadas desde Kaggle. Las imágenes presentan variaciones en iluminación, nitidez y niveles de ruido. Están en formato `.jpg` y se ubicaron dentro del directorio `data/input`.

---

## 4. Herramientas Utilizadas

- **Python 3.10+**
- **Pillow**: Para lectura y manipulación de imágenes.
- **NumPy**: Para operaciones matriciales y cálculos numéricos.
- **OpenCV (cv2)**: Para aplicar ciertos filtros como Sobel.
- **argparse**: Para construir una interfaz de línea de comandos simple.

---

## 5. Estructura del Proyecto

PDI_PROJECT/
│
├── data/
│ ├── input/ # Imágenes originales
│ └── output/ # Imágenes procesadas
│
├── src/
│ ├── core/ # Lógica de representación de imágenes
│ ├── io/ # Entrada/Salida de imágenes
│ ├── preprocessing/ # Filtros individuales (brillo, gaussian, etc.)
│ ├── restoration/ # Restaurador principal
│ ├── cli.py # CLI basada en argparse
│ └── main.py # Punto de entrada principal
│
├── informe_tecnico.md
├── README.md
└── requirements.txt


## 6. Metodología

### 6.1 Programación Orientada a Objetos

Cada componente del sistema fue diseñado como una clase individual con una responsabilidad clara:

- `Image`: Representa la imagen y facilita su manipulación.
- `ImageReader`: Encargada de la lectura y escritura de imágenes.
- Filtros: Cada uno en una clase separada (`BrightnessAdjuster`, `GaussianFilter`, `HistogramEqualizer`, `SobelFilter`).
- `ImageRestorer`: Clase orquestadora que aplica filtros de manera secuencial.

### 6.2 Filtros Utilizados

- **Ajuste de brillo**: Permite compensar la pérdida de luminosidad.
- **Filtro gaussiano**: Reduce el ruido suavemente.
- **Ecualización de histograma**: Mejora el contraste general.
- **Filtro de Sobel**: Resalta bordes y detalles.

---

## 7. Resultados

Se procesaron las 29 imágenes aplicando los filtros anteriores de forma secuencial. Se observó una mejora perceptible en el contraste y detalle de las imágenes. En algunos casos, se recuperaron detalles borrosos o zonas oscuras. El sistema permite guardar las imágenes restauradas en el directorio `data/output`.

---

## 8. Conclusiones

Este proyecto permitió aplicar múltiples conceptos vistos en clase, tales como representación matricial de imágenes, filtros espaciales, operaciones de convolución y ecualización. Se desarrolló un sistema completo, extensible y organizado, ideal para realizar futuros experimentos con otros filtros o conjuntos de datos.

---

## 9. Trabajo Futuro

- Implementación de detección automática de zonas degradadas.
- Mejora del rendimiento usando procesamiento por lotes o multithreading.
- Inclusión de una GUI simple con Tkinter o PyQt.
