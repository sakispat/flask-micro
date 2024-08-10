from flask import current_app as app
from flask import request, jsonify
from service.data import get_db_connection


@app.route('/products', methods=['GET'])
def get_products():
    connect = get_db_connection()
    cursor = connect.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products')
    users = cursor.fetchall()
    cursor.close()
    connect.close()
    return jsonify(users)


@app.route('/products', methods=['POST'])
def create_product():
    new_product = request.json
    connect = get_db_connection()
    cursor = connect.cursor()
    cursor.execute('INSERT INTO products (name, price) VALUES (%s, %s)', 
                   (new_product['name'], new_product['price']))
    connect.commit()
    cursor.close()
    connect.close()
    return jsonify(new_product), 201
