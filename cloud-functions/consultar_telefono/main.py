import functions_framework
from google.cloud import spanner
import json

from flask import Flask, request, jsonify
# Función para manejar las respuestas con formato JSON
def json_response(data, status_code):
    return (json.dumps(data), status_code, {'Content-Type': 'application/json'})


@functions_framework.http
def read_record(request):
    instance_id = 'taxiya'
    database_id = 'taxiya'

    # Instantiate a client.
    spanner_client = spanner.Client()

    # Get a Cloud Spanner instance by ID.
    instance = spanner_client.instance(instance_id)

    try:
        # Get a Cloud Spanner database by ID.
        database = instance.database(database_id)
        
        data = request.get_json()
        telefono = data['sessionInfo']['parameters']['telefono']

        if not telefono:
            return json_response({'error': 'Parámetro "telefono" faltante'}, 400)

        # Execute a simple SQL statement.
        with database.snapshot() as snapshot:
            results = snapshot.execute_sql(
                f'SELECT nombre, direccion FROM solicitudes WHERE telefono = {telefono}'
            )
            # Convertir los resultados en una lista de diccionarios
            rows = []
            for row in results:
                row_dict = {
                    'nombre': row[0],
                    'direccion': row[1]
                }
                direccion = row[1]
                rows.append(row_dict)
        if rows:
            message = "Desea un taxi a la direccion " + direccion + "?"
        else: 
            message = "Por favor diga taxi si desea solicitar un nuevo servicio"
        
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
        return json_response({'error': 'Error interno del servidor'}, 500)
