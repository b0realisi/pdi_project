# src/preprocessing/bilateral_filter.py 

import cv2
from src.core.image import Image

class BilateralFilter:
    def __init__(self, sigma_color: int = 75, sigma_space: int = 75):
        self.sigma_color = sigma_color
        self.sigma_space = sigma_space

    def apply(self, image: Image) -> Image:
        array = image.to_array()
        filtered = cv2.bilateralFilter(array, d=9, sigmaColor=self.sigma_color, sigmaSpace=self.sigma_space)
        return Image.from_array(filtered, mode=image.mode)