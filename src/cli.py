# src/cli.py
# este script procesa los argumentos desde la linea de comandos usando argparse

import argparse

def parse_arguments():
    """
    Crea y retorna los argumentos de línea de comandos.

    Devuelve un objeto con:
    - input_path: ruta de la imagen a procesar
    - output_path: ruta donde se guardará la imagen procesada
    """
    parser = argparse.ArgumentParser(
        description="Mejora o restauración de imágenes antiguas"
    )


    parser.add_argument("--input", type=str, required=True, help="Ruta de la imagen de entrada")
    parser.add_argument("--output", type=str, required=True, help="Ruta de la imagen de salida")

    # Filtros disponibles
    parser.add_argument("--brightness", action="store_true", help="Aplicar ajuste de brillo")
    parser.add_argument("--brightness-factor", type=float, default=1.0, help="Factor de brillo (por defecto 1.0)")

    parser.add_argument("--equalize", action="store_true", help="Aplicar ecualización de histograma")
    parser.add_argument("--clahe", action="store_true", help="Aplica ecualización de histograma adaptativa")
    parser.add_argument("--clahe-clipLimit", type=float, default=2.0, help="Límite de clip para CLAHE")
    parser.add_argument("--clahe-tileGridSize", type=int, nargs='+', default=[8, 8], help="Tamaño de la grilla para CLAHE (ej: 8 8)")

    parser.add_argument("--gaussian", action="store_true", help="Aplicar filtro gaussiano")
    parser.add_argument("--gaussian-kernel", type=int, default=5, help="Tamaño del kernel gaussiano (debe ser impar)")
    parser.add_argument("--median", action="store_true", help="Aplica filtro de mediana para reducir ruido")
    parser.add_argument("--median-kernel", type=int, default=3, help="Tamaño del kernel para el filtro de mediana")
    parser.add_argument("--bilateral", action="store_true", help="Aplica filtro bilateral para reducir ruido y preservar bordes")
    parser.add_argument("--bilateral-sigmaColor", type=int, default=75, help="SigmaColor para filtro bilateral")
    parser.add_argument("--bilateral-sigmaSpace", type=int, default=75, help="SigmaSpace para filtro bilateral")

    parser.add_argument("--sobel", action="store_true", help="Aplicar detección de bordes con Sobel")

    parser.add_argument("--colorize", action="store_true", help="Colorización artificial (experimental)") # activa la colorización
    parser.add_argument("--color-map", type=str, default="jet", help="Nombre del mapa de color para --colorize (jet, bone, pink, ocean, hot, cool)") # funcionará si --colorize está activo

    parser.add_argument("--grayscale", action="store_true", help="Convierte la imagen a escala de grises")

    parser.add_argument("--sharpen", action="store_true", help="Aplica filtro de nitidez")

    parser.add_argument("--inpaint", action="store_true", help="Aplica inpainting para eliminar imperfecciones")
    parser.add_argument("--inpaint-radius", type=int, default=3, help="Radio para la técnica de inpainting")
    parser.add_argument("--mask", type=str, help="Ruta a la imagen de máscara para usar con --inpaint")

    parser.add_argument("--grayscale", action="store_true", help="Convertir a escala de grises")
    parser.add_argument("--median", action="store_true") + "--median-kernel"
    parser.add_argument("--bilateral", action="store_true") + "--bilateral-sigmaColor" / "--bilateral-sigmaSpace"

    # Si no se elige ningún filtro, se aplica todo excepto Sobel
    return parser.parse_args()
