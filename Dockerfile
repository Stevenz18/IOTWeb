# Usa una imagen base de Python
FROM python:3.11-slim

# Instala las dependencias del sistema necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de tu aplicación a /app
COPY . /app

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que Flask corre (por defecto 5000)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
