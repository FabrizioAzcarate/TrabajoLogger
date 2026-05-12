from flask import Flask, jsonify, request
import logging
import random

# Crear aplicación Flask
app = Flask(__name__)

# Base de datos simulada en memoria
fake_database = []

# Configuración del sistema de logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

# GET /status/200
@app.route('/status/200', methods=['GET'])
def status_200():
    try:
        logger.info("GET /status/200 ejecutado correctamente")
        return jsonify({
            "message": "hola mundo"
        }), 200
    except Exception as error:
        logger.error(f"Error en GET /status/200: {error}")
        return jsonify({
            "message": "unexpected error"
        }), 500

# GET /status/500
@app.route('/status/500', methods=['GET'])
def status_500():
    try:
        logger.error("GET /status/500 devolvió internal server error")
        return jsonify({
            "message": "internal server error"
        }), 500

    except Exception as error:
        logger.error(f"Error en GET /status/500: {error}")
        return jsonify({
            "message": "unexpected error"
        }), 500

# GET /status/429
@app.route('/status/429', methods=['GET'])
def status_429():
    try:
        logger.warning("GET /status/429 devolvió too many requests")
        return jsonify({
            "message": "too many requests"
        }), 429

    except Exception as error:
        logger.error(f"Error en GET /status/429: {error}")
        return jsonify({
            "message": "unexpected error"
        }), 500

# POST /status/save
@app.route('/status/save', methods=['POST'])
def save_data():
    try:
        # Obtener JSON recibido
        data = request.get_json()

        # Validar que exista JSON
        if data is None:
            logger.warning("POST /status/save sin JSON válido")
            return jsonify({
                "message": "invalid json"
            }), 400

        # Simulación de error de base de datos
        if random.random() < 0.5:
            logger.error("Error simulado al guardar en la base de datos")
            return jsonify({
                "message": "database error"
            }), 500

        # Guardar en base de datos simulada
        fake_database.append(data)
        logger.info("Registro guardado correctamente")
        return jsonify({
            "message": "saved successfully",
            "data": data
        }), 201

    except Exception as error:
        logger.exception(f"Excepción en POST /status/save: {error}")
        return jsonify({
            "message": "unexpected error"
        }), 500

# GET /status/save
@app.route('/status/save', methods=['GET'])
def get_saved_data():
    try:
        logger.info("Consulta de registros guardados")
        return jsonify({
            "data": fake_database
        }), 200

    except Exception as error:
        logger.exception(f"Excepción en GET /status/save: {error}")
        return jsonify({
            "message": "unexpected error"
        }), 500

# Ruta principal opcional
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "API REST funcionando correctamente"
    }), 200

# Iniciar servidor
if __name__ == '__main__':
    logger.info("Servidor ejecutándose en http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)