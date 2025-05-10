# src/main.py
# Entrada principal: aplica los filtros seleccionados vía CLI y guarda la imagen resultante.

import cv2
from src.cli import parse_arguments
from src.io.image_reader import ImageReader
from src.core.image import Image

# Filtros modulares (POO)
from src.preprocessing.brightness_adjuster import BrightnessAdjuster
from src.preprocessing.gaussian_filter import GaussianFilter
from src.preprocessing.histogram_equalizer import HistogramEqualizer
from src.preprocessing.sobel_filter import SobelFilter
from src.preprocessing.false_colorer import FalseColorer
from src.preprocessing.sharpen_filter import SharpenFilter
from src.preprocessing.contrast_adjuster import ContrastAdjuster
from src.preprocessing.inpaint_filter import InpaintFilter
from src.preprocessing.clahe_filter import CLAHEFilter
from src.preprocessing.grayscale_converter import GrayscaleConverter
from src.preprocessing.median_filter import MedianFilter
from src.preprocessing.bilateral_filter import BilateralFilter

def main():
    args = parse_arguments()

    reader = ImageReader()
    image = reader.read(args.input)
    current_image = image

    applied_filters = []

    # Aplicación de filtros condicionales
    if args.brightness:
        current_image = BrightnessAdjuster(args.brightness_factor).apply(current_image)
        applied_filters.append(f"Brillo (factor={args.brightness_factor})")

    if args.equalize:
        current_image = HistogramEqualizer().apply(current_image)
        applied_filters.append("Ecualización de histograma")

    if args.gaussian:
        current_image = GaussianFilter(args.gaussian_kernel).apply(current_image)
        applied_filters.append(f"Suavizado Gaussiano (kernel={args.gaussian_kernel})")

    if args.sobel:
        current_image = SobelFilter().apply(current_image)
        applied_filters.append("Filtro Sobel")

    if args.colorize:
        current_image = FalseColorer(args.color_map).apply(current_image)
        applied_filters.append(f"Colorización ({args.color_map})")

    if args.grayscale:
        current_image = GrayscaleConverter().apply(current_image)
        applied_filters.append("Escala de grises")

    if args.median:
        current_image = MedianFilter(args.median_kernel).apply(current_image)
        applied_filters.append(f"Filtro de mediana (kernel={args.median_kernel})")

    if args.bilateral:
        current_image = BilateralFilter(args.bilateral_sigmaColor, args.bilateral_sigmaSpace).apply(current_image)
        applied_filters.append(f"Filtro bilateral (sigmaColor={args.bilateral_sigmaColor}, sigmaSpace={args.bilateral_sigmaSpace})")

    if args.sharpen:
        current_image = SharpenFilter().apply(current_image)
        applied_filters.append("Filtro de nitidez")

    if args.clahe:
        clahe = CLAHEFilter(clipLimit=args.clahe_clipLimit, tileGridSize=tuple(args.clahe_tileGridSize))
        current_image = clahe.apply(current_image)
        applied_filters.append(f"CLAHE (clipLimit={args.clahe_clipLimit}, grid={args.clahe_tileGridSize})")

    if args.inpaint:
        inpaint_filter = InpaintFilter(radius=args.inpaint_radius, mask_path=args.mask)
        current_image = inpaint_filter.apply(current_image)


    if args.contrast:
        current_image = ContrastAdjuster(alpha=args.contrast_alpha).apply(current_image)
        applied_filters.append(f"Contraste (alpha={args.contrast_alpha})")

    # Si no se pasa ningún filtro, aplicar mejoras suaves por defecto
    if not any([
        args.brightness, args.equalize, args.gaussian, args.sobel, args.colorize,
        args.grayscale, args.median, args.bilateral, args.sharpen, args.clahe,
        args.inpaint, args.contrast
    ]):
        current_image = BrightnessAdjuster(1.05).apply(current_image)
        current_image = HistogramEqualizer().apply(current_image)
        current_image = GaussianFilter(5).apply(current_image)
        applied_filters.append("Pipeline por defecto: Brillo + Ecualización + Gaussiano")

    # Guardar imagen final
    reader.save(current_image, args.output)
    print(f"\n Imagen procesada guardada en: {args.output}")
    print("Filtros aplicados:")
    for f in applied_filters:
        print(f" - {f}")

if __name__ == "__main__":
    main()
