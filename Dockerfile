FROM python:3.9-slim
WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY download_images.py ./

# Creamos la carpeta output para montarla después
RUN mkdir /app/output

# Lanzamos el downloader al iniciar el contenedor
CMD ["python", "download_images.py"]
