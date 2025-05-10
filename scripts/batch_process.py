# scripts/batch_process.py

import os
from src.io.image_reader import ImageReader
from src.restoration.image_enhancer import ImageEnhancer

INPUT_DIR = "data/input"
OUTPUT_DIR = "data/output"

def batch_process():
    reader = ImageReader()
    enhancer = ImageEnhancer(brightness_factor=1.05)

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.jpg', '.png', '.jpeg')):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, filename.replace(".jpg", "_mejorada.jpg"))

            image = reader.read(input_path)
            enhanced = enhancer.enhance(image)
            reader.save(enhanced, output_path)
            print(f"Guardado: {output_path}")

if __name__ == "__main__":
    batch_process()
