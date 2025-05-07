# src/restoration/image_restorer.py

from src.core.image import Image
from src.preprocessing.brightness_adjuster import BrightnessAdjuster
from src.preprocessing.gaussian_filter import GaussianFilter
from src.preprocessing.histogram_equalizer import HistogramEqualizer
from src.preprocessing.sobel_filter import SobelFilter

class ImageRestorer:
    def __init__(self, brightness_factor: float = 1.2, kernel_size: int = 5):
        """
        Inicializa el restaurador de imágenes con parámetros predeterminados.
        
        brightness_factor: factor de ajuste de brillo (ej. 1.2 para aumentar)
        kernel_size: tamaño del kernel para el filtro gaussiano (debe ser impar)
        """
        self.brightness_adjuster = BrightnessAdjuster(brightness_factor)  # Instancia del ajustador de brillo
        self.gaussian_filter = GaussianFilter(kernel_size)  # Instancia del filtro Gaussiano
        self.histogram_equalizer = HistogramEqualizer()  # Instancia del ecualizador de histograma
        self.sobel_filter = SobelFilter()  # Instancia del filtro de Sobel (bordes)

    def restore(self, image: Image) -> Image:
        """
        Aplica todos los pasos de restauración en orden:
        1. Ajuste de brillo
        2. Ecualización de histograma
        3. Suavizado con filtro Gaussiano
        4. Realce de bordes con Sobel
        """
        restored = self.brightness_adjuster.apply(image)  # Paso 1: ajustamos el brillo
        restored = self.histogram_equalizer.apply(restored)  # Paso 2: mejoramos el contraste
        restored = self.gaussian_filter.apply(restored)  # Paso 3: reducimos el ruido
        restored = self.sobel_filter.apply(restored)  # Paso 4: detectamos bordes
        return restored  # Devolvemos la imagen restaurada
