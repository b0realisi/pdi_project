# src/preprocessing/clahe_filter.py
import cv2
from src.core.image import Image
import numpy as np

class CLAHEFilter:
    """
    Aplica la ecualización de histograma adaptativa (CLAHE).
    """
    def __init__(self, clipLimit: float = 2.0, tileGridSize: tuple = (8, 8)):
        """
        Inicializa el filtro CLAHE.

        Args:
            clipLimit: Límite para el contraste en las regiones vecinas.
            tileGridSize: Tamaño de las regiones para la ecualización.
        """
        self.clipLimit = clipLimit
        self.tileGridSize = tileGridSize

    def apply(self, image: Image) -> Image:
        """
        Aplica CLAHE a la imagen.

        Args:
            image: La imagen de entrada.

        Returns:
            La imagen con CLAHE aplicado.
        """
        array = image.to_array()
        if len(array.shape) > 2:
            lab = cv2.cvtColor(array, cv2.COLOR_RGB2LAB)
            l, a, b = cv2.split(lab)
            clahe = cv2.createCLAHE(clipLimit=self.clipLimit, tileGridSize=self.tileGridSize)
            l = clahe.apply(l)
            lab = cv2.merge((l, a, b))
            result = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
            return Image.from_array(result, mode=image.mode)
        else:
            clahe = cv2.createCLAHE(clipLimit=self.clipLimit, tileGridSize=self.tileGridSize)
            adjusted = clahe.apply(array)
            return Image.from_array(adjusted, mode=image.mode)