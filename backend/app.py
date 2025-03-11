from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)  # <-- This is the key part


conn = psycopg2.connect(
    host = "db",
    port = 5432,
    database = "mydb",
    user = "user",
    password = "pass"  # Replace with your actual password!
)

# app
@app.route('/api')
def hello():
    return jsonify({'message': 'Hello, Backend!'})

@app.route('/users')
def get_users():
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    cur.close()
    users = [{"id": row[0], "name": row[1]} for row in rows]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0", port = 5000)