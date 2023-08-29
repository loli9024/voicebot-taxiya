import functions_framework
from google.cloud import spanner_v1
import json

from flask import Flask, request, jsonify

# Función para manejar las respuestas con formato JSON
def json_response(data, status_code):
    return (json.dumps(data), status_code, {'Content-Type': 'application/json'})

@functions_framework.http
def create_record(request):
    instance_id = 'taxiya'
    database_id = 'taxiya'
    client = spanner_v1.Client()

    instance = client.instance(instance_id)
    database = instance.database(database_id)

    try:
        # Recuperar los datos de la solicitud POST
        data = request.get_json()
        telefono = int(data['sessionInfo']['parameters']['telefono'])
        nombre = data['sessionInfo']['parameters']['nombre']
        direccion = data['sessionInfo']['parameters']['direccion']
        

        if not telefono or not nombre or not direccion:
            return json_response({'error': 'Datos incompletos'}, 400)

        with database.batch() as batch:
            batch.insert(
                table='solicitudes',
                columns=['telefono', 'nombre', 'direccion'],
                values=[(telefono, nombre, direccion)]
            )
        message = "Solicitud registrada con exito, su taxi va en camino a la direccion "+ direccion

        jsonResponse = {
            "fulfillment_response": {
                "messages": [
                    {
                        "text": {
                            "text": [message]
                        }
                    }
                ]
            }
        }
        return jsonify(jsonResponse), 200
    except Exception as e:
        print('unexpected error', e)
        jsonResponse = {
            "fulfillment_response": {
                "messages": [
                    {
                        "text": {
                            "text": [e]
                        }
                    }
                ]
            }
        }
        return jsonify(jsonResponse), 500
