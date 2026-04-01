from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="mydb",
        user="user",
        password="password"
    )
    return conn

@app.route('/')
def home():
    return "CI/CD Working 🔥"

@app.route('/data')
def data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return f"Database Time: {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)