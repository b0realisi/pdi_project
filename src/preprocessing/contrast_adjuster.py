# src/preprocessing/contrast_adjuster.py
import cv2
import numpy as np
from src.core.image import Image

class ContrastAdjuster:
    """
    Ajusta el contraste de la imagen.
    """
    def __init__(self, alpha: float = 1.0, beta: float = 0.0):
        """
        Inicializa el ajustador de contraste.

        Args:
            alpha: Factor de contraste (alpha > 1 aumenta el contraste, alpha < 1 lo disminuye).
            beta: Ajuste de brillo adicional (se añade a cada píxel después de aplicar alpha).
        """
        self.alpha = alpha
        self.beta = beta

    def apply(self, image: Image) -> Image:
        """
        Aplica el ajuste de contraste a la imagen.

        Args:
            image: La imagen de entrada.

        Returns:
            La imagen con el contraste ajustado.
        """
        array = image.to_array().astype(np.float32)
        adjusted = np.clip(self.alpha * array + self.beta, 0, 255).astype(np.uint8)
        return Image.from_array(adjusted, mode=image.mode)