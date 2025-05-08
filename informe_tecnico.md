# Informe Técnico - Proyecto Final de Procesamiento Digital de Imágenes

## Integrantes
- Gabriel Jourdan
- Ximena Macías
- Verónica Navón
- Nadia Ortiz
- Laura Poggio

## Carrera: Tecnicatura en Ciencia de Datos e Inteligencia Artificial  
## Materia: Procesamiento Digital de Imágenes  
## Cuatrimestre: 1C - 2025

---

## 1. Introducción

El presente proyecto tiene como objetivo aplicar técnicas de procesamiento digital de imágenes (PDI) para mejorar la calidad visual de fotografías antiguas. Estas imágenes, debido a su antigüedad y condiciones de almacenamiento, suelen presentar problemas como bajo contraste, desenfoque o ruido. El trabajo se enfoca en mejorar estas condiciones y posee un diseño modular basado en programación orientada a objetos.
La restauración de imágenes no solo tiene valor histórico y cultural, sino que también es una excelente aplicación de los conceptos fundamentales vistos durante la cursada. 

---

## 2. Objetivo

Desarrollar un sistema flexible que permita restaurar o mejorar visualmente imágenes antiguas a través de filtros seleccionables por el usuario desde una interfaz de línea de comandos (CLI).

---

## 3. Dataset

Se utilizó un conjunto de 29 imágenes antiguas descargadas desde Kaggle. Las imágenes presentan variaciones en iluminación, nitidez y niveles de ruido. Están en formato `.jpg` y se ubicaron dentro del directorio `data/input`.

---

## 4. Herramientas Utilizadas

- **Python 3.13+**
- **Pillow**: Para lectura y manipulación de imágenes.
- **NumPy**: Para operaciones matriciales y cálculos numéricos.
- **OpenCV (cv2)**: Para aplicar ciertos filtros como Sobel.
- **argparse**: Para construir una interfaz de línea de comandos simple.

---

## 5. Estructura del Proyecto

```nPDI_PROJECT/`n│`n├── data/`n│   ├── input/         # Imágenes originales`n│   └── output/        # Imágenes procesadas`n│`n├── src/`n│   ├── core/                  # Clase base Image`n│   ├── io/                    # Lector y escritor de imágenes`n│   ├── preprocessing/         # Filtros individuales`n│   ├── restoration/           # Clases orquestadoras (ImageRestorer, ImageEnhancer)`n│   ├── cli.py                 # CLI basada en argparse`n│   └── main.py                # Punto de entrada principal`n│`n├── README.md`n├── requirements.txt`n└── informe_tecnico.md`n````n`


## 6. Metodología


El proyecto se diseñó usando principios de programación orientada a objetos (POO), dividiendo la lógica en módulos reutilizables y especializados. El sistema puede operar de dos formas:

### a) Restauración completa (modo automático)
Aplica los siguientes filtros en orden:
1. Ajuste de brillo
2. Ecualización de histograma
3. Suavizado gaussiano  
> El filtro de bordes (Sobel) fue removido del pipeline por defecto, ya que afectaba negativamente el resultado visual.

### b) Modo personalizado (con flags)
El usuario puede elegir cuáles filtros aplicar mediante la CLI:
- `--brightness`
- `--equalize`
- `--gaussian`
- `--sobel`

---

## 7. Resultados

Se aplicaron los filtros sobre todas las imágenes del dataset. En modo automático, las imágenes mejoraron significativamente en contraste y visibilidad sin pérdida de detalle. En algunos casos, el uso opcional de Sobel permitió resaltar bordes, aunque no se recomienda como parte del pipeline por defecto.

El sistema permite guardar las imágenes restauradas en el directorio `data/output`.

---

## 8. Conclusiones

Este proyecto permitió aplicar múltiples conceptos vistos en clase. Se desarrolló un sistema completo, extensible y organizado, ideal para realizar futuros experimentos con otros filtros o conjuntos de datos. La arquitectura modular permite fácilmente agregar nuevos filtros o ajustar los existentes.

---

## 9. Implementaciones pendientes

- Implementación de detección automática de zonas degradadas.
- Inclusión de una GUI simple con Tkinter o PyQt.
- Permitir configurar parámetros como intensidad de brillo, sigma gaussiano o umbral de bordes desde la CLI.
- Agregar visualización de cada paso del pipeline.
- Integrar métricas objetivas (PSNR, SSIM) para comparar original vs restaurada.
