# src/preprocessing/brightness_adjuster.py

# Modifica la intensidad de los px para mejorar la visibilidad general de la imagen.

import numpy as np
from src.core.image import Image

class BrightnessAdjuster:
    def __init__(self, factor: float):
        """
        Inicializa el ajustador con un factor de brillo.
        Un valor >1 aumenta el brillo, <1 lo reduce.
        """
        self.factor = factor

    def apply(self, image: Image) -> Image:
        """
        Aplica el ajuste de brillo a la imagen dada.
        """
        array = image.to_array().astype(np.float32)  # Convertimos a float para evitar errores de saturación
        array *= self.factor  # Multiplicamos todos los valores de los píxeles por el factor
        array = np.clip(array, 0, 255).astype(np.uint8)  # Aseguramos que los valores estén entre 0 y 255
        return Image.from_array(array)  # Devolvemos una nueva imagen con el brillo ajustado
