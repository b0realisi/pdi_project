# src/main.py
# Este script conecta todo: lectura, restauración y guardado de la imagen.

from src.cli import parse_arguments
from src.io.image_reader import ImageReader
from src.restoration.image_restorer import ImageRestorer

def main():
    # Parseamos los argumentos desde la terminal
    args = parse_arguments()

    # Creamos una instancia del lector de imágenes
    reader = ImageReader()

    # Leemos la imagen desde el archivo de entrada
    image = reader.read(args.input)

    # Creamos una instancia del restaurador con parámetros por defecto
    restorer = ImageRestorer()

    # Restauramos la imagen aplicando los filtros en orden
    restored_image = restorer.restore(image)

    # Guardamos la imagen restaurada en la ruta de salida especificada
    reader.save(restored_image, args.output)

    print(f"Imagen restaurada guardada en {args.output}")

if __name__ == "__main__":
    main()
