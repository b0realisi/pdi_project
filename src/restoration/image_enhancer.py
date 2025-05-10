# src/restoration/image_enhancer.py
# Este archivo no se utiliza actualmente desde la CLI, pero puede ser usado como módulo auxiliar o de prueba

from src.core.image import Image
from src.preprocessing.brightness_adjuster import BrightnessAdjuster
from src.preprocessing.gaussian_filter import GaussianFilter
from src.preprocessing.histogram_equalizer import HistogramEqualizer

class ImageEnhancer:
    def __init__(self, brightness_factor: float = 1.0, kernel_size: int = 5):
        """
        Inicializa el mejorador de imágenes con parámetros opcionales.
        """
        self.brightness_adjuster = BrightnessAdjuster(brightness_factor)
        self.gaussian_filter = GaussianFilter(kernel_size)
        self.histogram_equalizer = HistogramEqualizer()

    def enhance(self, image: Image) -> Image:
        """
        Aplica las mejoras estéticas sin detección de bordes.
        """
        enhanced = self.brightness_adjuster.apply(image)
        enhanced = self.histogram_equalizer.apply(enhanced)
        enhanced = self.gaussian_filter.apply(enhanced)
        return enhanced
