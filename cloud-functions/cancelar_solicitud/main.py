import functions_framework
from google.cloud import spanner
import json

from flask import Flask, request, jsonify

# Función para manejar las respuestas con formato JSON
def json_response(data, status_code):
    return (json.dumps(data), status_code, {'Content-Type': 'application/json'})

@functions_framework.http
def delete_record(request):
    # Configuración de la instancia de Cloud Spanner
    instance_id = 'taxiya'
    database_id = 'taxiya'
    client = spanner.Client()
    instance = client.instance(instance_id)
    database = instance.database(database_id)
    try:
        
        data = request.get_json()
        telefono = int(data['sessionInfo']['parameters']['telefono'])  
        
        solicitudes = spanner.KeySet(keys=[(telefono,)])
        with database.batch() as batch:
            batch.delete("solicitudes", solicitudes)
        
        jsonResponse = {
            "fulfillment_response": {
                "messages": [
                    {
                        "text": {
                            "text": ["Su direccion ha sido actualizada, desea continuar solicitando un servicio de taxi?"]
                        }
                    }
                ]
            }
        }
        return jsonify(jsonResponse), 200
    except Exception as e:
        print('unexpected error', e)
        return json_response({'error': 'Error interno del servidor'}, 500)