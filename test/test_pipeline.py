# tests/test_basic_pipeline.py
# Prueba simple usando pytest para verificar el pipeline mínimo

import os
from src.io.image_reader import ImageReader
from src.core.image import Image
from src.preprocessing.brightness_adjuster import BrightnessAdjuster

def test_brightness_pipeline(tmp_path):
    # Cargar una imagen de ejemplo
    input_path = "data/input/old_photo_01.jpg"
    output_path = tmp_path / "output.jpg"

    reader = ImageReader()
    image = reader.read(input_path)

    # Aplicar un filtro simple
    processed = BrightnessAdjuster(1.1).apply(image)

    # Guardar la imagen procesada
    reader.save(processed, str(output_path))

    # Verificar que el archivo se creó
    assert output_path.exists()

    # Verificar que tiene las mismas dimensiones
    new_image = reader.read(str(output_path))
    assert new_image.to_array().shape == image.to_array().shape