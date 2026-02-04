from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os
import logging

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME")
    )

@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()
    logging.info(f"Received contact data: {data}")

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
      INSERT INTO contacts (name, email, message)
      VALUES (%s, %s, %s)
    """
    cursor.execute(query, (
        data["name"],
        data["email"],
        data["message"]
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Message stored successfully"}), 200

@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
