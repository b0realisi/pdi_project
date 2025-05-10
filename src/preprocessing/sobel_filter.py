# src/preprocessing/sobel_filter.py

# Detección de los bordes en la imagen, resaltando las transiciones de intensidad.

import cv2
import numpy as np
from src.core.image import Image

class SobelFilter:
    def apply(self, image: Image) -> Image:
        """
        Aplica el filtro de Sobel para detectar bordes en la imagen.
        """
        array = image.to_array()  # Convertimos la imagen a array
        gray = cv2.cvtColor(array, cv2.COLOR_RGB2GRAY)  # Convertimos a escala de grises
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # Gradiente en eje X
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # Gradiente en eje Y
        magnitude = np.sqrt(sobelx**2 + sobely**2)  # Calculamos la magnitud del gradiente
        magnitude = np.uint8(np.clip(magnitude, 0, 255))  # Normalizamos valores
        sobel_rgb = cv2.cvtColor(magnitude, cv2.COLOR_GRAY2RGB)  # Convertimos a RGB para compatibilidad
        return Image.from_array(sobel_rgb)  # Devolvemos la imagen con bordes detectados
