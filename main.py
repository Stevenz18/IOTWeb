from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Configura la conexión a MySQL
app.config['MYSQL_HOST'] = 'mysql.railway.internal'
#Ip del XAMPP
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'QYruqXDRGGyBxlYXXcoMmaTSExlNQYxZ'
#Campo de contraseña vacio
app.config['MYSQL_DB'] = 'railway'
#Nombre de mi base de datos
mysql = MySQL(app)

# Ruta para insertar datos
@app.route('/insert_data', methods=['POST'])
def insert_data():
    # Obtener el valor enviado por el ESP32
    data = request.get_json()
    nombre_sensor = data.get('nombre_sensor')
    valor_sensor = data.get('valor_sensor')
    if valor_sensor is None or nombre_sensor is None:
        return jsonify({'error': 'No se proporcionó el nombre o valor del sensor'}), 400
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Conectar con MySQL e insertar el dato
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO medicinav1 (nombre_sensor,valor,current_time) VALUES (%s,%s.%s)", (nombre_sensor,valor_sensor,timestamp))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'Datos insertados correctamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para obtener datos
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM medicinav1 ORDER BY timestamp DESC LIMIT 100")
        rows = cursor.fetchall()
        cursor.close()

        # Formatear los datos en JSON
        data = []
        for row in rows:
            data.append({
                'medicion_num': row[0],
                'nombre_sensor': row[1],
                'valor': row[2],
                'timestamp': row[3].strftime('%Y-%m-%d %H:%M:%S')
            })
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
