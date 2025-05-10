# Definimos la imagen del contenedor

# Dockerfile
FROM python:3.10-slim

# Creación del directorio de trabajo
WORKDIR /app

# Copia de los archivos del proyecto
COPY . /app

# Instalación de dependencias
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Comando por defecto
ENTRYPOINT ["python", "-m", "src.main"]