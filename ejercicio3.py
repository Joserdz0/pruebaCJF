from flask import Flask, request, jsonify, send_file
import csv
import os
import codecs


app = Flask(__name__)

# Ruta del archivo CSV
csv_file = 'ejercicio3.csv'

# Endpoint GET /ejercicio/descarga/
@app.route('/ejercicio/descarga/', methods=['GET'])
def download_csv():
    format_type = request.args.get('formato')
    
    if format_type == 'csv':
        return send_file(csv_file, as_attachment=True, mimetype='text/csv')
    elif format_type == 'json':
        data = csv_to_json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Formato no válido. Debe ser csv o json.'}), 400

# Endpoint POST /ejercicio/descarga/
@app.route('/ejercicio/descarga/', methods=['POST'])
def download_csv_post():
    format_type = request.json.get('formato')

    if format_type == 'csv':
        return send_file(csv_file, as_attachment=True, mimetype='text/csv')
    elif format_type == 'json':
        data = csv_to_json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Formato no válido. Debe ser csv o json.'}), 400

# Función para convertir el archivo CSV a JSON
def csv_to_json():
    data = []
    with open(csv_file, 'r', encoding='utf-8-sig') as file:  # utf-8-sig para omitir el BOM
        reader = csv.DictReader(file, skipinitialspace=True)
        i = 1
        for row in reader:
            if i == 1:
                print(row)
            
            data.append(row)
            i += 1
    return data

if __name__ == '__main__':
    # Verificar si el archivo CSV existe
    if not os.path.isfile(csv_file):
        print(f'El archivo {csv_file} no existe. Por favor, asegúrate de que el archivo exista y tenga los datos correctos.')
    else:
        app.run()

