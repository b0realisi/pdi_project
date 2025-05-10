# src/preprocessing/gaussian_filter.py

# Suaviza la imagen para reducir el ruido y las pequeñas imperfecciones.

import cv2
from src.core.image import Image

class GaussianFilter:
    def __init__(self, kernel_size: int = 5):
        """
        Inicializa el filtro con un tamaño de kernel.
        El kernel debe ser impar y positivo (ej: 3, 5, 7).
        """
        self.kernel_size = kernel_size

    def apply(self, image: Image) -> Image:
        """
        Aplica el filtro gaussiano para suavizar la imagen.
        """
        array = image.to_array()  # Convertimos la imagen a array de NumPy
        blurred = cv2.GaussianBlur(array, (self.kernel_size, self.kernel_size), 0)  # Aplicamos el filtro
        return Image.from_array(blurred)  # Devolvemos la imagen suavizada
