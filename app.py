from flask import Flask, jsonify, request
import mysql.connector
from flasgger import Swagger
import os
from dotenv import load_dotenv
from decimal import Decimal
import json
from flask_cors import CORS
import requests

# Load environment variables from .env file
load_dotenv()

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


app = Flask(__name__)
CORS(app)
swagger = Swagger(app, template_file='swagger_doc.yml')
app.json_encoder = DecimalEncoder

# MySQL configuration
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE'),
}

@app.route('/get_all_products', methods=['GET'])
def get_all_products():
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Execute query
        cursor.execute('SELECT * FROM products')
        result = cursor.fetchall()

        # Format the result as JSON
        products = []
        for row in result:
            product = {
                'id': row[0],
                'name': row[1],
                'brand':row[2],
                'type':row[3],
                'price': row[4],
                'amount': row[5]
            }
            products.append(product)

        return jsonify(products), 200

    except mysql.connector.Error as error:
        return jsonify({'error': str(error)})

    finally:
        # Close the database connection
        cursor.close()
        connection.close()

@app.route('/get_address', methods=['GET'])
def get_address():
    try:
        # Retrieve the cep from the query parameters
        cep = request.args.get('cep')

        # make the request
        response  = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

        if response.status_code == 200:
            # Format the result as JSON
            data = response.json()
            return jsonify(data)
        else:
            # Format the result as JSON
            print(response)
            return jsonify({'error': 'Failed to fetch address data'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/insert_product', methods=['POST'])
def insert_product():
    try:
        # Retrieve product data from the request body
        product_data = request.get_json()
        name = product_data['name']
        brand = product_data['brand']
        type = product_data['type']
        price = product_data['price']
        amount = product_data['amount']

        # Connect to MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Execute query
        query = 'INSERT INTO products (name, brand, type, price, amount) VALUES (%s, %s,%s,%s, %s)'
        cursor.execute(query, (name, brand, type, price, amount))
        connection.commit()

        return jsonify({'message': 'Product inserted successfully'})

    except mysql.connector.Error as error:
        return jsonify({'error': str(error)})

    finally:
        # Close the database connection
        cursor.close()
        connection.close()

@app.route('/edit_product', methods=['PUT'])
def edit_product():
    try:
        # Retrieve product data from the request body
        product_data = request.get_json()
        id = product_data['id']
        name = product_data['name']
        brand = product_data['brand']
        type = product_data['type']
        price = product_data['price']
        amount = product_data['amount']

        # Connect to MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Execute query
        query = '''
            UPDATE products
            SET name = %s, brand = %s, type = %s, price = %s, amount = %s
            WHERE id = %s
        '''
        cursor.execute(query, (name, brand, type, price, amount, id))
        connection.commit()

        return jsonify({'message': 'Product replaced successfully'})

    except mysql.connector.Error as error:
        return jsonify({'error': str(error)})

    finally:
        # Close the database connection
        cursor.close()
        connection.close()

@app.route('/delete_product', methods=['DELETE'])
def delete_product():
    try:
        # Retrieve product ID from the query parameters
        product_id = request.args.get('id')

        # Connect to MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Execute query
        query = 'DELETE FROM products WHERE id = %s'
        cursor.execute(query, (product_id,))
        connection.commit()

        return jsonify({'message': 'Product deleted successfully'})

    except mysql.connector.Error as error:
        return jsonify({'error': str(error)})

    finally:
        # Close the database connection
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run()
