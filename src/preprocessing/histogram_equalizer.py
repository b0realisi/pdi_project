# src/preprocessing/histogram_equalizer.py

import cv2
import numpy as np
from src.core.image import Image

class HistogramEqualizer:
    def apply(self, image: Image) -> Image:
        """
        Aplica ecualización del histograma por canal para mejorar el contraste.
        """
        array = image.to_array()  # Obtenemos el array de la imagen
        ycrcb = cv2.cvtColor(array, cv2.COLOR_RGB2YCrCb)  # Convertimos a espacio YCrCb
        ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])  # Ecualizamos solo el canal Y (luminancia)
        result = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2RGB)  # Convertimos de nuevo a RGB
        return Image.from_array(result)  # Devolvemos la imagen con contraste mejorado
