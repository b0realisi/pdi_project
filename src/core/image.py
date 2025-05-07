# src/core/image.py

from PIL import Image as PILImage
import numpy as np

class Image:
    def __init__(self, pil_image: PILImage.Image, filename: str = None):
        self._image = pil_image
        self.filename = filename

    @classmethod
    def from_array(cls, array: np.ndarray):
        pil_image = PILImage.fromarray(array)
        return cls(pil_image)

    def to_array(self) -> np.ndarray:
        return np.array(self._image)

    def show(self):
        self._image.show()

    def save(self, path: str):
        self._image.save(path)

    @property
    def pil(self) -> PILImage.Image:
        return self._image

    def copy(self):
        return Image(self._image.copy(), self.filename)
