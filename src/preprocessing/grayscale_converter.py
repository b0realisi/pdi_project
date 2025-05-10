# src/preprocessing/grayscale_converter.py ===

from src.core.image import Image

class GrayscaleConverter:
    def apply(self, image: Image) -> Image:
        gray = cv2.cvtColor(image.to_array(), cv2.COLOR_RGB2GRAY)
        return Image.from_array(gray, mode="L")


# === src/preprocessing/median_filter.py ===
import cv2
from src.core.image import Image

class MedianFilter:
    def __init__(self, kernel_size: int = 3):
        self.kernel_size = kernel_size

    def apply(self, image: Image) -> Image:
        array = image.to_array()
        filtered = cv2.medianBlur(array, self.kernel_size)
        return Image.from_array(filtered, mode=image.mode)