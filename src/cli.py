# src/cli.py
# este script procesa los argumentos desde la linea de comandos usando argparse

import argparse

def parse_arguments():
    """
    Crea y retorna los argumentos de línea de comandos.

    Devuelve un objeto con:
    - input_path: ruta de la imagen a procesar
    - output_path: ruta donde se guardará la imagen procesada
    """
    parser = argparse.ArgumentParser(
        description="Procesamiento y restauración de imágenes antiguas"
    )

    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Ruta de la imagen de entrada (por ejemplo: data/input/foto1.jpg)"
    )

    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Ruta de salida para guardar la imagen restaurada (por ejemplo: data/output/foto1_restaurada.jpg)"
    )

    return parser.parse_args()  # Devuelve un objeto con los argumentos parseados
