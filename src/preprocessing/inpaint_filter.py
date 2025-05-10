# src/preprocessing/inpaint_filter.py
import cv2
import numpy as np
from src.core.image import Image

class InpaintFilter:
    """
    Aplica la técnica de inpainting para reconstruir áreas dañadas de la imagen.

    Si no se provee una máscara externa, se aplica una máscara de demostración (rectángulo fijo).
    """
    def __init__(self, radius: int = 3, method: int = cv2.INPAINT_TELEA, mask_path: str = None):
        """
        Inicializa el filtro de inpainting.

        Args:
            radius: Radio del área a considerar para el inpainting.
            method: Método de inpainting a utilizar (cv2.INPAINT_NS o cv2.INPAINT_TELEA).
            mask_path: Ruta a una imagen de máscara externa en blanco y negro.
        """
        self.radius = radius
        self.method = method
        self.mask_path = mask_path

    def apply(self, image: Image) -> Image:
        """
        Aplica el inpainting a la imagen.

        Args:
            image: La imagen de entrada.

        Returns:
            La imagen con las áreas dañadas reconstruidas.
        """
        array = image.to_array()

        if self.mask_path:
            mask = cv2.imread(self.mask_path, cv2.IMREAD_GRAYSCALE)
            if mask is None or mask.shape[:2] != array.shape[:2]:
                raise ValueError("La máscara no existe o no coincide en dimensiones con la imagen de entrada.")
        else:
            # Máscara de demostración
            mask = np.zeros(array.shape[:2], dtype=np.uint8)
            mask[10:50, 20:80] = 255  # Rectángulo fijo de prueba

        inpainted = cv2.inpaint(array, mask, self.radius, self.method)
        return Image.from_array(inpainted, mode=image.mode)
