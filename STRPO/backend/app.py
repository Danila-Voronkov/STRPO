
import os
import psycopg2
from flask import Flask, request, jsonify
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host='db',
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        cursor_factory=RealDictCursor
    )
    return conn

@app.route('/api/sensors', methods=['GET'])
def get_sensors():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM sensors ORDER BY id;')
    sensors = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(sensors)

@app.route('/api/sensors', methods=['POST'])
def create_sensor():
    data = request.get_json()
    name = data.get('name')
    plant_name = data.get('plant_name')
    value = data.get('value')
    unit = data.get('unit')
    if not all([name, plant_name, value, unit]):
        return jsonify({'error': 'Missing fields'}), 400
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO sensors (name, plant_name, value, unit) VALUES (%s, %s, %s, %s) RETURNING *;',
        (name, plant_name, value, unit)
    )
    new_sensor = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(new_sensor), 201

@app.route('/api/sensors/<int:id>', methods=['DELETE'])
def delete_sensor(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM sensors WHERE id = %s RETURNING *;', (id,))
    deleted = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if deleted:
        return jsonify({'message': 'Sensor deleted', 'sensor': deleted})
    else:
        return jsonify({'error': 'Sensor not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)