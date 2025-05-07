# src/io/image_reader.py

from PIL import Image as PILImage
from src.core.image import Image
import os

class ImageReader:
    @staticmethod
    def read(path: str) -> Image:
        try:
            pil_image = PILImage.open(path).convert("RGB")
            return Image(pil_image, filename=os.path.basename(path))
        except Exception as e:
            raise IOError(f"No se pudo abrir la imagen: {path}. Error: {e}")

    @staticmethod
    def save(image: Image, path: str):
        try:
            image.save(path)
        except Exception as e:
            raise IOError(f"No se pudo guardar la imagen: {path}. Error: {e}")
