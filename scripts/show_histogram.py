# scripts/show_histogram.py

import cv2
import matplotlib.pyplot as plt
from src.io.image_reader import ImageReader
from src.preprocessing.histogram_equalizer import HistogramEqualizer

def plot_histogram(image_array, title="Histograma"):
    colors = ('r', 'g', 'b')
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image_array], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
    plt.title(title)
    plt.xlabel('Intensidad')
    plt.ylabel('Frecuencia')
    plt.xlim([0, 256])

# Cargar imagen original
reader = ImageReader()
image = reader.read("data/input/old_photo_21.jpg")
array_original = image.to_array()

# Procesar
equalizer = HistogramEqualizer()
image_eq = equalizer.apply(image)
array_eq = image_eq.to_array()

# Mostrar histogramas
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plot_histogram(array_original, "Antes de ecualizar")
plt.subplot(1, 2, 2)
plot_histogram(array_eq, "Después de ecualizar")
plt.tight_layout()
plt.show()
