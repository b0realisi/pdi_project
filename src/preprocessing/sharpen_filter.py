# src/preprocessing/sharpen_filter.py
import cv2
import numpy as np
from src.core.image import Image

class SharpenFilter:
    """
    Aplica un filtro de nitidez a la imagen.
    """
    def apply(self, image: Image) -> Image:
        """
        Aplica el filtro de nitidez a la imagen.

        Args:
            image: La imagen de entrada.

        Returns:
            La imagen con el filtro de nitidez aplicado.
        """
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
        array = cv2.filter2D(image.to_array(), -1, kernel)
        return Image.from_array(array, mode=image.mode)