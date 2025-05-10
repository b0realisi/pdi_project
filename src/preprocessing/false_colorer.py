# src/preprocessing/false_colorer.py

import cv2
import numpy as np
from src.core.image import Image

class FalseColorer:
    def __init__(self, colormap: str = "jet"):
        self.colormap = self.get_colormap_code(colormap)

    def get_colormap_code(self, name: str) -> int:
        name = name.lower()
        colormaps = {
            "jet": cv2.COLORMAP_JET,
            "bone": cv2.COLORMAP_BONE,
            "pink": cv2.COLORMAP_PINK,
            "ocean": cv2.COLORMAP_OCEAN,
            "hot": cv2.COLORMAP_HOT,
            "cool": cv2.COLORMAP_COOL
        }
        return colormaps.get(name, cv2.COLORMAP_JET)  # default to jet

    def apply(self, image: Image) -> Image:
        gray = cv2.cvtColor(image.to_array(), cv2.COLOR_RGB2GRAY)
        color_mapped = cv2.applyColorMap(gray, self.colormap)
        color_rgb = cv2.cvtColor(color_mapped, cv2.COLOR_BGR2RGB)
        return Image.from_array(color_rgb)
