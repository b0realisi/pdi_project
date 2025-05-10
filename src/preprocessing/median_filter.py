# src/preprocessing/median_filter.py 

import cv2
from src.core.image import Image

class MedianFilter:
    def __init__(self, kernel_size: int = 3):
        self.kernel_size = kernel_size

    def apply(self, image: Image) -> Image:
        array = image.to_array()
        filtered = cv2.medianBlur(array, self.kernel_size)
        return Image.from_array(filtered, mode=image.mode)