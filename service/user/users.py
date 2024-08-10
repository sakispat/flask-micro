from flask import current_app as app
from flask import request, jsonify
from service.data import get_db_connection


@app.route('/users', methods=['GET'])
def get_users():
    connect = get_db_connection()
    cursor = connect.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    connect.close()
    return jsonify(users)


@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    connect = get_db_connection()
    cursor = connect.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', 
                   (new_user['name'], new_user['email']))
    connect.commit()
    cursor.close()
    connect.close()
    return jsonify(new_user), 201
