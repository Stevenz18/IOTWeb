# Usa una imagen base de Python 3.11
FROM python:3.11-slim

# Instala dependencias del sistema necesarias para MySQL
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev gcc pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de la aplicación a /app
COPY . .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que Flask corre (por defecto 5000)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
